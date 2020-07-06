from flask import Flask, render_template
from flask import request,send_file
app = Flask(__name__)

@app.route('/todos/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        input = './' + f.filename
        output = './output.txt'

        table = input.split('/')[-1].split('.')[0]
        with open(input, encoding='utf-8') as f:
            with open(output, 'w', encoding='utf-8') as g:
                contents = "Insert into " + table + "("
                i = 0
                for row in f:
                    if i == 0:
                        typeList = row.rstrip().split(',')
                    if i == 1:
                        columList = row.rstrip().split(',')
                        k = 0
                        for c in columList:
                            if len(columList) == k + 1:
                                contents = contents + c + 'VALUES ('
                            else:
                                contents = contents + c + ','
                            k = k + 1
                        basecontets = contents
                    if i >= 2:
                        j = 0
                        for r in row.rstrip().split(','):
                            if not 'INTEGER' in typeList[j]:
                                r = "'" + r + "'"
                            if len(row.rstrip().split(',')) == j + 1:
                                basecontets = basecontets + r
                            else:
                                basecontets = basecontets + r + ','
                            j = j + 1
                        basecontets = basecontets + ');' + '\n'
                        g.write(basecontets)
                        basecontets = contents
                    i = i + 1
            print("作成完了しました")
    return render_template('index.html')

@app.route('/download')
def download_file():

	path = './output.txt'
	return send_file(path, as_attachment=True)



@app.route('/')
def index():
  return render_template('index.html')


