#!/bin/bash


# For OSX development
if [[ `uname` == "Darwin" ]]; then
    script_directory=$(dirname "$0")

    brew update
    echo "Installing Postgres"
    brew install postgresql
    brew services start postgresql
    echo "Installing Redis"
    brew install redis
    brew services start redis

else
    script_directory=$(dirname $(readlink -f $BASH_SOURCE))

    sudo apt-get update
    sudo apt-get install screen git gh python3 virtualenv postgresql-all redis
    sudo service postgresql start
    sudo service redis start
fi

source $script_directory/config.rc
sudo -u postgres createdb $DBNAME
sudo -u postgres psql -c "CREATE USER $DBUSER WITH ENCRYPTED PASSWORD '$DBPASSWORD';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DBNAME to $DBUSER;"
sudo -u postgres psql -c "ALTER DATABASE $DBNAME OWNER TO $DBUSER;"

mkdir $script_directory/tmp
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
