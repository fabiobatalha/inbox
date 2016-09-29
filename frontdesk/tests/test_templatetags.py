from unittest import TestCase
from django.template import Template, Context


class TemplatetagsTest(TestCase):

    def test_status_color_default(self):

        template = Template(
            "{% load status_colors %} {{ status|status_color }}")

        rendered = template.render(Context({}))

        self.assertIn('grey', rendered)

    def test_status_color_infected(self):

        template = Template(
            "{% load status_colors %} {{ status|status_color }}")

        rendered = template.render(Context({'status': 'infected'}))

        self.assertIn('red', rendered)

    def test_status_color_unknow(self):

        template = Template(
            "{% load status_colors %} {{ status|status_color }}")

        rendered = template.render(Context({'status': 'unknow'}))

        self.assertIn('grey', rendered)

    def test_status_color_rejected(self):

        template = Template(
            "{% load status_colors %} {{ status|status_color }}")

        rendered = template.render(Context({'status': 'rejected'}))

        self.assertIn('red', rendered)

    def test_status_color_uninfected(self):

        template = Template(
            "{% load status_colors %} {{ status|status_color }}")

        rendered = template.render(Context({'status': 'uninfected'}))

        self.assertIn('green', rendered)

    def test_status_color_deposited(self):

        template = Template(
            "{% load status_colors %} {{ status|status_color }}")

        rendered = template.render(Context({'status': 'deposited'}))

        self.assertIn('aqua', rendered)

    def test_status_color_queued(self):

        template = Template(
            "{% load status_colors %} {{ status|status_color }}")

        rendered = template.render(Context({'status': 'queued'}))

        self.assertIn('aqua', rendered)

    def test_status_color_accepted(self):

        template = Template(
            "{% load status_colors %} {{ status|status_color }}")

        rendered = template.render(Context({'status': 'accepted'}))

        self.assertIn('green', rendered)