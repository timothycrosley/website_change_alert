website_change_alert
_________________

[![PyPI version](https://badge.fury.io/py/website_change_alert.svg)](http://badge.fury.io/py/website_change_alert)
[![Test Status](https://github.com/timothycrosley/website_change_alert/workflows/Test/badge.svg?branch=develop)](https://github.com/timothycrosley/website_change_alert/actions?query=workflow%3ATest)
[![Lint Status](https://github.com/timothycrosley/website_change_alert/workflows/Lint/badge.svg?branch=develop)](https://github.com/timothycrosley/website_change_alert/actions?query=workflow%3ALint)
[![codecov](https://codecov.io/gh/timothycrosley/website_change_alert/branch/master/graph/badge.svg)](https://codecov.io/gh/timothycrosley/website_change_alert)
[![Join the chat at https://gitter.im/timothycrosley/website_change_alert](https://badges.gitter.im/timothycrosley/website_change_alert.svg)](https://gitter.im/timothycrosley/website_change_alert?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.python.org/pypi/website_change_alert/)
[![Downloads](https://pepy.tech/badge/website_change_alert)](https://pepy.tech/project/website_change_alert)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://timothycrosley.github.io/isort/)
_________________

[Read Latest Documentation](https://timothycrosley.github.io/website_change_alert/) - [Browse GitHub Code Repository](https://github.com/timothycrosley/website_change_alert/)
_________________

**website_change_alert** Script to quickly alert when a website changes.

This was built to quickly alert of website changes, primarily for to identify when new vaccine doses get posted on a sign up genius page.

In order to utilize you need a twilio account (a free account is fine), and any machine with the internet connected to run the script continuously.

Once the site is seen as having changed the script will send the given phone numbers the url and stop running.

It's recommended that you set your phone to always alert you when your twilio phone number sends you a text message to avoid missing the site change.
