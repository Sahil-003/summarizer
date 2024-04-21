from flask import Flask,render_template,request

from text_summary_function import summarizer

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/analyze',methods=['GET','POST'])
def analyze():
    if request.method == 'POST':
        rawtext=request.form['rawtext']
        summary,original_txt,org_len,summ_len=summarizer(rawtext)

    return render_template('summary.html',summary=summary,original_txt=original_txt,org_len=org_len,summ_len=summ_len)

if __name__ =="__main__":
    app.run(debug=True)