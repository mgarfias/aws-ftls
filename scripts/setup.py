#!/usr/bin/python2.6

import mimetypes
import os
import boto
from boto.s3.connection import S3Connection
from boto.ec2.connection import EC2Connection
from subprocess import call
import yaml


def create_bucket(conn, name):
    bucket = conn.create_bucket(name)
    
def get_s3_connection():
    return S3Connection()

def get_bucket(conn, name):
    return conn.get_bucket(name)

def get_ctype(f):
    return mimetypes.guess_type(f)[0] or "application/x-octet-stream"
    
def put_file(filename, keyname):
    new_key = Key(bucket)
    new_key.key = keyname
    new_key.set_metadata('Content-Type', get_ctype(filename))
    new_key.set_contents_from_filename(filename)

# pull from config file
conffile = file("../config.yaml")
config = yaml.safe_load(conffile)

# create the s3 connection
s3_conn = S3Connection(config['aws_access_key_id'],config['aws_secret_access_key'])
bucket = get_bucket(conn, config['bucket_name'])    
# create ec2 connection
ec2_conn = EC2Connection(config['aws_access_key_id'],config['aws_secret_access_key'])

# check to see if the bucket exists, if not, create
# TODO
create_bucket(s3_conn,bucket_name)

# call s3cmd to install puppet files to s3
# need to figure out pwd and adjust the conf file, and path to the puppet files
#s3cmd -c ~/.s3cfg put --recursive -P ./puppet s3://puppet.garfias.org/

# spin up instances
num_instances=config['num_instances']
instance_count=0
for region in config['aws_region']:
    # connect to region
    c = boto.connect_to_region(region,config['aws_access_key_id'],config['aws_secret_access_key'])
    # fire up instance
    ec2_conn.run_instances(config['base_ami'],config['instance_type'])
    count++
    if count >= config['num_instances']
        break
        

# assign EIPs to instances
# add EIPs to route53