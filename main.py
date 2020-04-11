from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])

def index():
  return render_template("index.html")
    
@app.route('/form', methods=["GET","POST"])
def form():
  if request.method == "GET":
    return render_template("form.html")
  else: #POST
    #if request.
    name = request.form.get('name')
    level = request.form.get('schoolyear')
    Class = request.form.get('Class')
    register = request.form.get('registernumber')
    mobile = request.form.get('mobile')
    gender = request.form.get('gender')
    country = request.form.get('country')
    traveldate1 = request.form.get('traveldate1')
    traveldate2 = request.form.get('traveldate2')
    others = request.form.get('others')
    traveldate3 = request.form.get('traveldate3')
    traveldate4 = request.form.get('traveldate4')
    agreement = request.form.get('agreement')

    with open('data1.txt', 'a') as _file:
      _file.write(name)
      _file.write('\n')
      _file.write(level)      
      _file.write('\n')
      _file.write(Class)
      _file.write('\n')
      _file.write(register)
      _file.write('\n')
      _file.write(mobile)
      _file.write('\n')
      _file.write(gender)
      _file.write('\n')
      _file.write(country)
      _file.write('\n')
      _file.write(traveldate1)
      _file.write('\n')
      _file.write(traveldate2)
      _file.write('\n')
      _file.write(others)
      _file.write('\n')
      _file.write(traveldate3)
      _file.write('\n')
      _file.write(traveldate4)
      _file.write('\n')
      _file.write(agreement)
      _file.write('\n')
    return render_template("form.html", name=name, level=level, gender=gender, mobile=mobile, register=register, Class=Class, country=country, traveldate1=traveldate1, others=others, traveldate2=traveldate2, traveldate3=traveldate3, traveldate4=traveldate4, agreement=agreement)

@app.route('/easteregg')
def easter_egg():
  return render_template("easteregg.html")


app.run(host='0.0.0.0', port=8080)

