# src/services/product_service.py
from typing import List, Dict, Optional
from src.dao.product_dao import ProductDAO

class ProductError(Exception):
    """Custom exception for product-related errors."""
    pass

class ProductService:
    """Service class for managing products."""

    def __init__(self):
        self.product_dao = ProductDAO()

    def add_product(self, name: str, sku: str, price: float, stock: int = 0, category: Optional[str] = None) -> Dict:
        if price <= 0:
            raise ProductError("Price must be a positive number.")
        if self.product_dao.get_product_by_sku(sku):
            raise ProductError(f"Product with SKU '{sku}' already exists.")

        product = self.product_dao.create_product(name, sku, price, stock, category)
        if not product:
            raise ProductError("Failed to create the product.")
        return product

    def restock_product(self, prod_id: int, delta: int) -> Dict:
        if delta <= 0:
            raise ProductError("Quantity to add must be positive.")

        p = self.product_dao.get_product_by_id(prod_id)
        if not p:
            raise ProductError(f"Product with ID {prod_id} not found.")

        new_stock = (p.get("stock") or 0) + delta
        updated_product = self.product_dao.update_product(prod_id, {"stock": new_stock})
        if not updated_product:
            raise ProductError("Failed to update product stock.")
        return updated_product

    def get_low_stock(self, threshold: int = 5) -> List[Dict]:
        all_products = self.product_dao.list_products(limit=1000)
        return [p for p in all_products if (p.get("stock") or 0) <= threshold]