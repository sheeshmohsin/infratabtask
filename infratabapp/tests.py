import json
import datetime
from django.test import TestCase
from tastypie.test import TestApiClient

client = TestApiClient()

# Create your tests here.
class ApiTestCase(TestCase):

	def test_api_home(self):
		resp = client.get('/api/v1/')
		self.assertEqual(resp.status_code, 200)

	def test_api_emailnotf(self):
		resp = client.get('/api/v1/emailnotf/')
		self.assertEqual(resp.status_code, 200)

	def test_api_emailnotf_schema(self):
		resp = client.get('/api/v1/emailnotf/schema/')
		self.assertEqual(resp.status_code, 200)

	def test_api_reminder(self):
		resp = client.get('/api/v1/reminder/')
		self.assertEqual(resp.status_code, 200)

	def test_api_reminder_schema(self):
		resp = client.get('/api/v1/reminder/schema/')
		self.assertEqual(resp.status_code, 200)

	def test_api_smsnotf(self):
		resp = client.get('/api/v1/smsnotf/')
		self.assertEqual(resp.status_code, 200)

	def test_api_smsnotf_schema(self):
		resp = client.get('/api/v1/smsnotf/schema/')
		self.assertEqual(resp.status_code, 200)

	def test_api_reminder_save(self):
		datetimer = datetime.datetime.now() + datetime.timedelta(days=1)
		resp = client.post('/api/v1/reminder/', data={'datetime': datetimer.utcnow().isoformat(), 'message': 'test message'})
		self.assertEqual(resp.status_code, 201)
		resp = client.delete('/api/v1/reminder/', data={'datetime': datetimer.utcnow().isoformat(), 'message': 'test message'})
		self.assertEqual(resp.status_code, 204)

