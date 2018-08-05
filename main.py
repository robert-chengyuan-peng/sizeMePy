# import logging

#import


# Import User Authentication
from google.appengine.api import users

# Import WSGI
# from flask import Flask, render_template, request
import webapp2
# import urllib
# import jinja2
import logging
# user = users.get_current_user()

# if user:
# 	nickname = user.nickname()
# 	logout_url = users.create_logout_url('/')
# 	greeting = 'Hello, {}! (<a href="{}" sign out</a>)'.format(nickname, logout_url)



# app = Flask(__name__)



# @app.route('/form')
# def form():
# 	return render_template('form.html')


class MainPage(webapp2.RequestHandler):
	#mainpage req handler

	def get(self):
		user = users.get_current_user()
		if user:
			nickname = user.nickname()
			logout_url = users.create_logout_url('/')
			greeting = 'Hello, {}! (<a href="{}"> sign out</a>)'.format(nickname, logout_url)
		else:
			login_url = users.create_login_url('/')
			greeting = '<a href="{}"> sign in</a>'.format(login_url)

		self.response.write('<html><body>{}</body></html>'.format(greeting))


		# self.response.headers['Content-Type'] = 'text/plain'
		# self.response.write('Hello')
		logging.info('test')



class AdminPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('Hello')
		logging.info('test')





app = webapp2.WSGIApplication([
	('/',MainPage),
	('/admin', AdminPage)
	], debug = True)


#End