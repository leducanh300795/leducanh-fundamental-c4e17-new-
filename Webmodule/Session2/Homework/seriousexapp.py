from flask import Flask, render_template
import mlab
from module.customer import Customers
# from mongoengine import StringField,IntField,BooleanField,Document
from mongoengine import *
app = Flask(__name__)

mlab.connect()

# # design database
# #creat collection
# class Service(Document):
#     name = StringField()
#     yob = IntField()
#     gender = IntField()
#     height = IntField()
#     phone = StringField()
#     address = StringField()
#     status = BooleanField()
#
# service = Service(name= "Kiều Anh",
#                     yob= 1996,
#                     gender=0,
#                     height=163,
#                     phone="01236556789",
#                     address="Hai Bà Trưng - Hà Nội",
#                     status=True)
#
# service.save()
# service = Service(name= "Ngân Búng",
#                     yob= 1992,
#                     gender=1,
#                     height=165,
#                     phone="01236556789",
#                     address="Câu Giấy - Hà Nội",
#                     status=False)
#
# service.save()



@app.route('/')
def search():
    all_customer = Customers.objects()
    return render_template('search.html',
                            all_customer = all_customer)


@app.route('/customer')
def search_customer():
    all_customer = Customers.objects[0:10](contacted=False, gender =1)
    return render_template('searchcustomer.html', all_customer = all_customer)
# @app.route('/searchage/<age>')
# def search(age):
#     all_service = Service.objects(yob__lte)
#     return render_template('searchage.html',
#                             all_service = all_service)

# @app.route('/<id>')
# def searchid(id):
#     id_to_find = Service.objects.get(id=id)
#     return id_to_find

if __name__ == '__main__':
  app.run( debug=True)
