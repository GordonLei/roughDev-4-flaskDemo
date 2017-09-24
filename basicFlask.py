from flask import Flask

my_app = Flask(__name__)
@my_app.route('/')
def root():
        return "W o a h"
@my_app.route('/UpUpDownDownLeftRightLeftRightBAStart')
def spook():
        return "<html>Up<br><br>Up<br><br>Down<br><br>Down<br><br>Left<br><br>Right<br><br>Left<br><br>Right<br><br>B<br><br>A<br><br>Start<br><br><br>You been spooked by the Konami Code!</html>"
@my_app.route('/BlankPage')
def page():
        return "You were expecting a blank page but it was me, Page With Some Text That You Are Reading For Some Reason!"

if __name__ == '__main__':
        my_app.debug = True
        my_app.run()