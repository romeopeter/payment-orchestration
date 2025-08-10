from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.transaction_service import (
    create_transaction,
    list_customer_transactions,
)

# ------------------------------------------------------------------------------------------


txn_bp = Blueprint("transaction", __name__)


@txn_bp.route("/", methods=["POST"])
@jwt_required()
def create_txn():
    """
    Create a new transaction (Simulation)
    ---
    tags:
      - Transactions
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              amount:
                type: integer
              gateway:
                type: string
              txn_metadata:
                type: object
    responses:
      201:
        description: Transaction created
    """

    data = request.json
    customer_id = get_jwt_identity()
    txn = create_transaction(
        amount=data["amount"],
        gateway=data["gateway"],
        customer_id=customer_id,
        txn_metadata=["txn_metadata"],
    )
    data = {
        "gateway_ref": txn.gateway_ref,
        "status": txn.status,
        "amount": txn.amount,
        "gateway": txn.gateway,
        "created_at": txn.created_at.isoformat(),
    }
    return jsonify({"data": data, "message": "Transaction created", "status": 201})


@txn_bp.route("/", methods=["GET"])
@jwt_required()
def list_txns():
    """
    List transactions for the logged-in user
    ---
    tags:
        - Transactions
    responses:
        200:
            description: List of transactions
    """

    customer_id = get_jwt_identity()
    txns = list_customer_transactions(customer_id)
    data = [
        {
            "gateway_ref": t.gateway_ref,
            "amount": t.amount,
            "status": t.status,
            "gateway": t.gateway,
            "created_at": t.created_at.isoformat(),
        }
        for t in txns
    ]
    return jsonify({"data": data, "message": "List of transactions", "status": 201})
