from flask import render_template

from money_box import app


@app.route('/moneybox')
def moneybox():
    return render_template('money_box.html')