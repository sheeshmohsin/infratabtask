========================
Interacting With The API
========================

Api-Wide
--------

We'll start at the highest level::

    curl http://localhost:8000/api/v1/?format=json

You'll get back something like::

	{
	    "emailnotf": {
	        "list_endpoint": "/api/v1/emailnotf/",
	        "schema": "/api/v1/emailnotf/schema/"
	    },
	    "reminder": {
	        "list_endpoint": "/api/v1/reminder/",
	        "schema": "/api/v1/reminder/schema/"
	    },
	    "smsnotf": {
	        "list_endpoint": "/api/v1/smsnotf/",
	        "schema": "/api/v1/smsnotf/schema/"
	    }
	}
	
To demonstrate another format, you could run the following to get the XML
variant of the same information::

    curl -H "Accept: application/xml" http://localhost:8000/api/v1/
    
To which you'd receive::
    
	<response>
		<emailnotf type="hash">
			<list_endpoint>/api/v1/emailnotf/</list_endpoint>
			<schema>/api/v1/emailnotf/schema/</schema>
		</emailnotf>
		<reminder type="hash">
			<list_endpoint>/api/v1/reminder/</list_endpoint>
			<schema>/api/v1/reminder/schema/</schema>
		</reminder>
		<smsnotf type="hash">
			<list_endpoint>/api/v1/smsnotf/</list_endpoint>
			<schema>/api/v1/smsnotf/schema/</schema>
		</smsnotf>
	</response>
	
We'll stick to JSON for the rest of this document, but using XML should be OK
to do at any time.

It's also possible to get all schemas (`Inspecting The Resource's Schema`_) in a single request::

    curl http://localhost:8000/api/v1/?fullschema=true
    
You'll get back something like::
    
	{
	    "emailnotf": {
	        "list_endpoint": "/api/v1/emailnotf/",
	        "schema": {
	            "allowed_detail_http_methods": [
	                "get",
	                "post",
	                "put",
	                "delete",
	                "patch"
	            ],
	            "allowed_list_http_methods": [
	                "get",
	                "post",
	                "put",
	                "delete",
	                "patch"
	            ],
	            "default_format": "application/json",
	            "default_limit": 20,
	            "fields": {
	                "email": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "Unicode string data. Ex: \"Hello World\"",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": false,
	                    "type": "string",
	                    "unique": false,
	                    "verbose_name": "email"
	                },
	                "reminder": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "A single related resource. Can be either a URI or set of nested resource data.",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": false,
	                    "related_schema": "/api/v1/reminder/schema/",
	                    "related_type": "to_one",
	                    "type": "related",
	                    "unique": false,
	                    "verbose_name": "reminder"
	                },
	                "resource_uri": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "Unicode string data. Ex: \"Hello World\"",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": true,
	                    "type": "string",
	                    "unique": false,
	                    "verbose_name": "resource uri"
	                }
	            }
	        }
	    },
	    "reminder": {
	        "list_endpoint": "/api/v1/reminder/",
	        "schema": {
	            "allowed_detail_http_methods": [
	                "get",
	                "post",
	                "put",
	                "delete",
	                "patch"
	            ],
	            "allowed_list_http_methods": [
	                "get",
	                "post",
	                "put",
	                "delete",
	                "patch"
	            ],
	            "default_format": "application/json",
	            "default_limit": 20,
	            "fields": {
	                "datetime": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "A date & time as a string. Ex: \"2010-11-10T03:07:43\"",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": false,
	                    "type": "datetime",
	                    "unique": false,
	                    "verbose_name": "datetime"
	                },
	                "id": {
	                    "blank": true,
	                    "default": "",
	                    "help_text": "Integer data. Ex: 2673",
	                    "nullable": false,
	                    "primary_key": true,
	                    "readonly": false,
	                    "type": "integer",
	                    "unique": true,
	                    "verbose_name": "ID"
	                },
	                "message": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "Unicode string data. Ex: \"Hello World\"",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": false,
	                    "type": "string",
	                    "unique": false,
	                    "verbose_name": "message"
	                },
	                "resource_uri": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "Unicode string data. Ex: \"Hello World\"",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": true,
	                    "type": "string",
	                    "unique": false,
	                    "verbose_name": "resource uri"
	                }
	            }
	        }
	    },
	    "smsnotf": {
	        "list_endpoint": "/api/v1/smsnotf/",
	        "schema": {
	            "allowed_detail_http_methods": [
	                "get",
	                "post",
	                "put",
	                "delete",
	                "patch"
	            ],
	            "allowed_list_http_methods": [
	                "get",
	                "post",
	                "put",
	                "delete",
	                "patch"
	            ],
	            "default_format": "application/json",
	            "default_limit": 20,
	            "fields": {
	                "mobile": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "Unicode string data. Ex: \"Hello World\"",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": false,
	                    "type": "string",
	                    "unique": false,
	                    "verbose_name": "mobile"
	                },
	                "reminder": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "A single related resource. Can be either a URI or set of nested resource data.",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": false,
	                    "related_schema": "/api/v1/reminder/schema/",
	                    "related_type": "to_one",
	                    "type": "related",
	                    "unique": false,
	                    "verbose_name": "reminder"
	                },
	                "resource_uri": {
	                    "blank": false,
	                    "default": "No default provided.",
	                    "help_text": "Unicode string data. Ex: \"Hello World\"",
	                    "nullable": false,
	                    "primary_key": false,
	                    "readonly": true,
	                    "type": "string",
	                    "unique": false,
	                    "verbose_name": "resource uri"
	                }
	            }
	        }
	    }
	}
    

Inspecting The Resource's Schema
--------------------------------

Since the api-wide view gave us a ``schema`` URL, let's inspect that next.
We'll use the ``reminder`` resource. Again, a simple GET request by curl::

    curl http://localhost:8000/api/v1/reminder/schema/

This time, we get back a lot more data::


	{
	    "allowed_detail_http_methods": [
	        "get",
	        "post",
	        "put",
	        "delete",
	        "patch"
	    ],
	    "allowed_list_http_methods": [
	        "get",
	        "post",
	        "put",
	        "delete",
	        "patch"
	    ],
	    "default_format": "application/json",
	    "default_limit": 20,
	    "fields": {
	        "datetime": {
	            "blank": false,
	            "default": "No default provided.",
	            "help_text": "A date & time as a string. Ex: \"2010-11-10T03:07:43\"",
	            "nullable": false,
	            "primary_key": false,
	            "readonly": false,
	            "type": "datetime",
	            "unique": false,
	            "verbose_name": "datetime"
	        },
	        "id": {
	            "blank": true,
	            "default": "",
	            "help_text": "Integer data. Ex: 2673",
	            "nullable": false,
	            "primary_key": true,
	            "readonly": false,
	            "type": "integer",
	            "unique": true,
	            "verbose_name": "ID"
	        },
	        "message": {
	            "blank": false,
	            "default": "No default provided.",
	            "help_text": "Unicode string data. Ex: \"Hello World\"",
	            "nullable": false,
	            "primary_key": false,
	            "readonly": false,
	            "type": "string",
	            "unique": false,
	            "verbose_name": "message"
	        },
	        "resource_uri": {
	            "blank": false,
	            "default": "No default provided.",
	            "help_text": "Unicode string data. Ex: \"Hello World\"",
	            "nullable": false,
	            "primary_key": false,
	            "readonly": true,
	            "type": "string",
	            "unique": false,
	            "verbose_name": "resource uri"
	        }
	    }
	}
	
This lists out the ``default_format`` this resource responds with, the
``fields`` on the resource & the ``filtering`` options available. This
information can be used to prepare the other aspects of the code for the
data it can obtain & ways to filter the resources.

Getting A Collection Of Resources
---------------------------------

Let's get down to fetching live data. From the api-wide view, we'll hit
the ``list_endpoint`` for ``reminder``::

    curl http://localhost:8000/api/v1/reminder/

We get back data that looks like::


	{
	    "meta": {
	        "limit": 20,
	        "next": null,
	        "offset": 0,
	        "previous": null,
	        "total_count": 7
	    },
	    "objects": [
	        {
	            "datetime": "2016-08-09T18:51:48",
	            "id": 1,
	            "message": "Time to go infratab",
	            "resource_uri": "/api/v1/reminder/1/"
	        },
	        {
	            "datetime": "2016-08-10T22:31:59",
	            "id": 2,
	            "message": "its your time now",
	            "resource_uri": "/api/v1/reminder/2/"
	        },
	        {
	            "datetime": "2016-08-11T22:32:47",
	            "id": 3,
	            "message": "check",
	            "resource_uri": "/api/v1/reminder/3/"
	        },
	        {
	            "datetime": "2016-08-12T22:37:53",
	            "id": 4,
	            "message": "test1",
	            "resource_uri": "/api/v1/reminder/4/"
	        },
	        {
	            "datetime": "2016-08-13T22:38:45",
	            "id": 5,
	            "message": "test2",
	            "resource_uri": "/api/v1/reminder/5/"
	        },
	        {
	            "datetime": "2016-08-15T22:46:27",
	            "id": 6,
	            "message": "testing job",
	            "resource_uri": "/api/v1/reminder/6/"
	        },
	        {
	            "datetime": "2011-05-22T00:46:38",
	            "id": 7,
	            "message": "This will prbbly be my lst post.",
	            "resource_uri": "/api/v1/reminder/7/"
	        }
	    ]
	}
	
	
Some things to note:

  * By default, you get a paginated set of objects (20 per page is the default).
  * In the ``meta``, you get a ``previous`` & ``next``. If available, these are
    URIs to the previous & next pages.
  * You get a list of resources/objects under the ``objects`` key.
  * Each resources/object has a ``resource_uri`` field that points to the
    detail view for that object.
  * The foreign key to ``User`` is represented as a URI by default. If you're
    looking for the full ``UserResource`` to be embedded in this view, you'll
    need to add ``full=True`` to the ``fields.ToOneField``.

If you want to skip paginating, simply run::

    curl http://localhost:8000/api/v1/reminder/?limit=0

Be warned this will return all objects, so it may be a CPU/IO-heavy operation
on large datasets.


Getting A Detail Resource
-------------------------

Since each resource/object in the list view had a ``resource_uri``, let's
explore what's there::

    curl http://localhost:8000/api/v1/reminder/1/

We get back a similar set of data that we received from the list view::


	{
	    "datetime": "2016-08-09T18:51:48",
	    "id": 1,
	    "message": "Time to go infratab",
	    "resource_uri": "/api/v1/reminder/1/"
	}
	
Selecting A Subset Of Resources
-------------------------------

Sometimes you may want back more than one record, but not an entire list view
nor do you want to do multiple requests. This API includes a "set" view, which
lets you cherry-pick the objects you want. For example, if we just want the
first & third ``reminder`` resources, we'd run::

    curl "http://localhost:8000/api/v1/reminder/set/1;3/"

.. note::

  Quotes are needed in this case because of the semicolon delimiter between
  primary keys. Without the quotes, bash tries to split it into two statements.
  No extraordinary quoting will be necessary in your application (unless your
  API client is written in bash :D).

And we get back just those two objects::

	{
	    "objects": [
	        {
	            "datetime": "2016-08-09T18:51:48",
	            "id": 1,
	            "message": "Time to go infratab",
	            "resource_uri": "/api/v1/reminder/1/"
	        },
	        {
	            "datetime": "2016-08-11T22:32:47",
	            "id": 3,
	            "message": "check",
	            "resource_uri": "/api/v1/reminder/3/"
	        }
	    ]
	}
	
Note that, like the list view, you get back a list of ``objects``. Unlike the
list view, there is **NO** pagination applied to these objects. You asked for
them, you're going to get them all.

Creating A New Resource (POST)
------------------------------

Let's add a new reminder. To create new data, we'll switch from ``GET`` requests
to the familiar ``POST`` request.

.. note::

    API encourages "round-trippable" data, which means the data you
    can GET should be able to be POST/PUT'd back to recreate the same
    object.

    If you're ever in question about what you should send, do a GET on
    another object & see what API thinks it should look like.

To create new resources/objects, you will ``POST`` to the list endpoint of
a resource. Trying to ``POST`` to a detail endpoint has a different meaning in
the REST mindset (meaning to add a resource as a child of a resource of the
same type).

As with all API requests, the headers we request are important. Since
we've been using primarily JSON throughout, let's send a new reminder in JSON
format::

    curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"datetime": "some datetime", "message": "sample message"}' http://127.0.0.1:8080/api/v1/reminder/

The ``Content-Type`` header here informs API that we're sending it JSON.
We send the data as a JSON-serialized body (**NOT** as form-data in the form of
URL parameters). What we get back is the following response::

    HTTP/1.0 201 Created
	Date: Tue, 07 Jun 2016 10:27:11 GMT
	Server: WSGIServer/0.1 Python/2.7.6
	Vary: Accept
	X-Frame-Options: SAMEORIGIN
	Content-Type: application/json
	Location: /api/v1/reminder/2/

	{"datetime": "some datetime", "message": "sample message", "id": "2", "resource_uri": "/api/v1/reminder/2/"}

You'll also note that we get a correct HTTP status code back (201) & a
``Location`` header, which gives us the URI to our newly created resource.

Passing ``--dump-header -`` is important, because it gives you all the headers
as well as the status code. When things go wrong, this will be useful
information to help with debugging.


Updating An Existing Resource (PUT)
-----------------------------------

You might have noticed that we made some typos when we submitted the POST
request. We can fix this using a ``PUT`` request to the detail endpoint (modify
this instance of a resource).::

    curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"datetime":"some datetime", "message":"some sample message"}' http://127.0.0.1:8080/api/v1/reminder/2/

After fixing up the ``body``, we get back::

    HTTP/1.0 204 NO CONTENT
    Date: Fri, 20 May 2011 07:13:21 GMT
    Server: WSGIServer/0.1 Python/2.7
    Content-Length: 0
    Content-Type: text/html; charset=utf-8

We get a 204 status code, meaning our update was successful. We don't get
a ``Location`` header back because we did the ``PUT`` on a detail URL, which
presumably did not change.

.. note::

    A ``PUT`` request requires that the entire resource representation be enclosed. Missing fields may cause errors, or be filled in by default values.
    

Partially Updating An Existing Resource (PATCH)
-----------------------------------------------

In some cases, you may not want to send the entire resource when updating. To update just a subset of the fields, we can send a ``PATCH`` request to the detail endpoint.::

    curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"message":"updating message"}' http://127.0.0.1:8080/api/v1/reminder/2/


To which we should get back::

    HTTP/1.0 202 ACCEPTED
    Date: Fri, 20 May 2011 07:13:21 GMT
    Server: WSGIServer/0.1 Python/2.7
    Content-Length: 0
    Content-Type: text/html; charset=utf-8

Deleting Data
=============

No CRUD setup would be complete without the ability to delete resources/objects.
Deleting also requires significantly less complicated requests than
``POST``/``PUT``.

Deleting A Single Resource
--------------------------

We've decided that we don't like the provider we added & edited earlier. Let's
delete it (but leave the other objects alone)::

    curl --dump-header - -H "Content-Type: application/json" -X DELETE  http://localhost:8000/api/v1/reminder/2/

Once again, we get back the "Accepted" response of a 204::

    HTTP/1.0 204 NO CONTENT
    Date: Fri, 20 May 2011 07:28:01 GMT
    Server: WSGIServer/0.1 Python/2.7
    Content-Length: 0
    Content-Type: text/html; charset=utf-8
    
We can also use smsnotification, emailnotification model api in above format
-----------------------------------------------------------------------------


