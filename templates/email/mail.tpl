{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello Ben
{% endblock %}

{% block body %}
 this is a plain text message.
{% endblock %}

{% block html %}
 this is an <strong>html</strong> message.
{% endblock %}