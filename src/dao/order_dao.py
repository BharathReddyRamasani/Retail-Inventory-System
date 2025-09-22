# src/dao/order_dao.py
from typing import List, Dict, Optional
from src.config import get_supabase

class OrderDAO:
    """Data Access Object for orders and order_items."""

    def __init__(self):
        self._sb = get_supabase()

    def create_order(self, cust_id: int, items: List[Dict], total_amount: float) -> Optional[Dict]:
        """Insert order and order_items atomically."""

        # 1️⃣ Insert order and get its ID back in one step
        order_payload = {
            "cust_id": cust_id,
            "total_amount": total_amount,
            "status": "PLACED"
        }
        order_insert_resp = self._sb.table("orders").insert(order_payload).execute()
        if not order_insert_resp.data:
            return None
        order_id = order_insert_resp.data[0]["order_id"]

        # 2️⃣ Prepare and insert all order items
        order_items_payload = [
            {
                "order_id": order_id,
                "prod_id": item["prod_id"],
                "quantity": item["quantity"],
                "price": item["price"]  # Price at the time of order
            } for item in items
        ]
        
        if order_items_payload:
            self._sb.table("order_items").insert(order_items_payload).execute()

        return self.get_order_details(order_id)

    def get_order_details(self, order_id: int) -> Optional[Dict]:
        """Return order info with customer and items."""
        resp = self._sb.table("orders").select(
            "*, customer:customers(*), items:order_items(*, product:products(*))"
        ).eq("order_id", order_id).maybe_single().execute()
        
        return resp.data if resp.data else None

    def list_orders_by_customer(self, cust_id: int) -> List[Dict]:
        resp = self._sb.table("orders").select("*").eq("cust_id", cust_id).execute()
        return resp.data or []

    def update_order_status(self, order_id: int, status: str) -> Optional[Dict]:
        resp = self._sb.table("orders").update({"status": status}).eq("order_id", order_id).execute()
        if resp.data:
            return self.get_order_details(order_id)
        return None