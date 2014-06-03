Setup Guide
===========

This setup is not only about software installation but also about configuration.
It is recommended that you explore the software you install.

Prerequisite (General)
----------------------

You Don't Say?

# `Setup Python 3`__
# `Setup Git`_
# `Setup VirtualEnv`_
# `Setup VirtualEnvWrapper`_
# `Setup Sqlite3`_

Prerequisite (For Server)
----------------------

# `Setup Redis`_
# `Setup PostgreSQL`_
# `Setup ElasticSearch`_


Installation
------------

.. code-block:: sh

    # project virtual environment
    mkvirtualenv bsapi -p python3
    workon bsapi

    # Clone project
    git clone git@github.com:9gix/bsapi.git

    cd bsapi

    # Install package dependencies
    pip install -r requirements.txt

    # Create Database
    python manage.py syncdb
    python manage.py migrate

    # Run Test
    python manage.py test

    # Runserver
    python manage.py runserver



.. _Setup Python 3: https://wiki.python.org/moin/BeginnersGuide/Download
.. _Setup Git: http://virtualenvwrapper.readthedocs.org/en/latest/install.html
.. _Setup VirtualEnv: http://virtualenvwrapper.readthedocs.org/en/latest/install.html
.. _Setup VirtualEnvWrapper: http://virtualenvwrapper.readthedocs.org/en/latest/install.html
.. _Setup Sqlite3: http://www.sqlite.org/download.html
.. _Setup PostgreSQL: https://wiki.postgresql.org/wiki/Detailed_installation_guides
.. _Setup Redis: http://redis.io/download
.. _Setup ElasticSearch: http://www.elasticsearch.org/overview/elasticsearch/