from app.extensions import db
from app.models.transaction_model import Transaction
import uuid

# ------------------------------------------------------


def generate_reference():
    return "txn_" + uuid.uuid4().hex[:10]


def create_transaction(amount, gateway, customer_id, metadata=None):
    reference = generate_reference()
    txn = Transaction(
        reference=reference,
        amount=amount,
        gateway=gateway,
        status="pending",
        customer_id=customer_id,
        metadata=metadata or {},
    )
    db.session.add(txn)
    db.session.commit()
    return txn


def get_transaction_by_reference(reference):
    return Transaction.query.filter_by(reference=reference).first()


def list_customer_transactions(customer_id):
    return (
        Transaction.query.filter_by(customer_id=customer_id)
        .order_by(Transaction.created_at.desc())
        .all()
    )
