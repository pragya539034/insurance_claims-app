from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def submit_claim():
    if request.method == "POST":
        policy_number = request.form.get("policy_number")
        claim_type = request.form.get("claim_type")
        claim_amount = request.form.get("claim_amount")
        description = request.form.get("description")
        document = request.files.get("document")

        print("Policy Number:", policy_number)
        print("Type of Claim:", claim_type)
        print("Claim Amount:", claim_amount)
        print("Description:", description)
        if document:
            print("Document Uploaded:", document.filename)

        return "✅ Claim submitted successfully!"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5009,debug=True)
