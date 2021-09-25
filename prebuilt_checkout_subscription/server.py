import stripe
import os
from flask import Flask, redirect, request


stripe.api_key = "api_key"

app = Flask(__name__, static_url_path="", static_folder=".")

YOUR_DOMAIN = "http://localhost:4242"


@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():
    try:
        # The price ID passed from the front end.
        price_id = request.form.get("priceId")

        session = stripe.checkout.Session.create(
            success_url=YOUR_DOMAIN + "/success.html",
            cancel_url=YOUR_DOMAIN + "/cancel.html",
            payment_method_types=["card"],
            mode="subscription",
            line_items=[
                {
                    "price": price_id,
                    # For metered billing, do not pass quantity
                    "quantity": 1,
                }
            ],
        )
    except Exception as e:
        return str(e)

    # Redirect to the URL returned on the session
    return redirect(session.url, code=303)


if __name__ == "__main__":
    app.run(port=4242)
