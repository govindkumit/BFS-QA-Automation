from fastapi import FastAPI, HTTPException

app = FastAPI(title="BFS Mini Banking API")

accounts = {
    "1001": {"name": "John", "balance": 10000},
    "1002": {"name": "David", "balance": 5000},
}


@app.get("/")
def home():
    return {"message": "BFS Banking API is running"}


@app.get("/accounts/{account_id}")
def get_account(account_id: str):
    if account_id not in accounts:
        raise HTTPException(status_code=404, detail="Account not found")

    return accounts[account_id]


@app.post("/transfer")
def transfer(sender: str, receiver: str, amount: float):

    if sender not in accounts or receiver not in accounts:
        raise HTTPException(status_code=404, detail="Account not found")

    if amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")

    if accounts[sender]["balance"] < amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    accounts[sender]["balance"] -= amount
    accounts[receiver]["balance"] += amount

    return {
        "status": "SUCCESS",
        "sender": sender,
        "receiver": receiver,
        "amount": amount
    }