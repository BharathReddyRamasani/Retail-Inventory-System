# src/services/customer_service.py
from typing import List, Dict, Optional
from src.dao.customer_dao import CustomerDAO

class CustomerError(Exception):
    pass

class CustomerService:
    def __init__(self):
        self.customer_dao = CustomerDAO()

    def create_customer(self, name: str, email: str, phone: str, city: Optional[str] = None) -> Dict:
        try:
            customer = self.customer_dao.create_customer(name, email, phone, city)
            if not customer:
                 raise CustomerError("Failed to create customer.")
            return customer
        except ValueError as e:
            raise CustomerError(str(e))

    def update_customer(self, cust_id: int, phone: Optional[str] = None, city: Optional[str] = None) -> Dict:
        if not self.customer_dao.get_customer_by_id(cust_id):
            raise CustomerError(f"Customer with ID {cust_id} not found.")
        
        fields = {}
        if phone:
            fields["phone"] = phone
        if city:
            fields["city"] = city
        
        if not fields:
            raise CustomerError("No fields provided to update.")
        
        updated_customer = self.customer_dao.update_customer(cust_id, fields)
        if not updated_customer:
            raise CustomerError("Failed to update customer.")
        return updated_customer

    def delete_customer(self, cust_id: int) -> Dict:
        try:
            deleted_customer = self.customer_dao.delete_customer(cust_id)
            if not deleted_customer:
                raise CustomerError(f"Customer with ID {cust_id} not found or could not be deleted.")
            return deleted_customer
        except ValueError as e:
            raise CustomerError(str(e))

    def list_customers(self) -> List[Dict]:
        return self.customer_dao.list_customers()

    def search_customers(self, email: Optional[str] = None, city: Optional[str] = None) -> List[Dict]:
        return self.customer_dao.search_customers(email=email, city=city)