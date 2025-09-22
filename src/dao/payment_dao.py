# src/dao/payment_dao.py
from src.config import get_supabase
from datetime import datetime
from typing import Optional, Dict, Union

class PaymentDAO:
    def __init__(self):
        self._sb = get_supabase()

    def create_payment(self, order_id: int, amount: float) -> Optional[Dict]:
        payload = {
            "order_id": order_id,
            "amount": amount,
            "status": "PENDING"
        }
        resp = self._sb.table("payments").insert(payload).execute()
        return resp.data[0] if resp.data else None

    def update_payment(
        self,
        order_id: int,
        status: str,
        method: Optional[str] = None,
        paid_at: Optional[Union[datetime, str]] = None,
    ) -> Optional[Dict]:
        payload = {"status": status}
        if method:
            payload["method"] = method
        if paid_at:
            if isinstance(paid_at, datetime):
                payload["paid_at"] = paid_at.isoformat()
            else:
                payload["paid_at"] = paid_at

        resp = self._sb.table("payments").update(payload).eq("order_id", order_id).execute()
        return resp.data[0] if resp.data else None

    def get_payment(self, order_id: int) -> Optional[Dict]:
        resp = self._sb.table("payments").select("*").eq("order_id", order_id).limit(1).execute()
        return resp.data[0] if resp.data else None