from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
claims_data = []

@app.route("/")
def home():
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    return render_template(
        "index.html",   # dashboard page
        total_claims=len(claims_data),
        pending=sum(1 for c in claims_data if c["status"] == "Pending"),
        approved=sum(1 for c in claims_data if c["status"] == "Approved"),
        rejected=sum(1 for c in claims_data if c["status"] == "Rejected"),
    )

@app.route("/new-claim", methods=["GET", "POST"])
def new_claim():
    if request.method == "POST":
        claims_data.append({
            "id": len(claims_data) + 1,
            "policy_number": request.form.get("policy_number"),
            "type": request.form.get("claim_type"),
            "amount": request.form.get("claim_amount"),
            "description": request.form.get("description"),
            "status": "Pending"
        })
        return redirect(url_for("claims"))
    return render_template("new-claim.html")

@app.route("/claims")
def claims():
    return render_template("claims.html", claims=claims_data)

@app.route("/reports")
def reports():
    summary = {
        "total": len(claims_data),
        "pending": sum(1 for c in claims_data if c["status"] == "Pending"),
        "approved": sum(1 for c in claims_data if c["status"] == "Approved"),
        "rejected": sum(1 for c in claims_data if c["status"] == "Rejected"),
    }
    return render_template("reports.html", summary=summary)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


