import pandas as pd
import pymysql
import logging
import sshtunnel
from sshtunnel import SSHTunnelForwarder
import paramiko


ssh_host = 'ec2-18-208-120-207.compute-1.amazonaws.com'
ssh_username = 'ubuntu'
ssh_password = 'SecretPassword'
database_name = 'datacrunch'
endpoint = 'mwsmaster-dtc-r.cfx5gks3rioa.us-east-1.rds.amazonaws.com'
database_username = 'yanjie_zheng'
database_password = '4pGp37bvNnjHEejb'



pkey='../data_science.pem'
key=paramiko.RSAKey.from_private_key_file(pkey)

def open_ssh_tunnel(verbose=False):
    """Open an SSH tunnel and connect using a username and password.

    :param verbose: Set to True to show logging
    :return tunnel: Global SSH tunnel connection
    """

    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG

    global tunnel
    tunnel = SSHTunnelForwarder(
        (ssh_host, 22),
        ssh_username=ssh_username,
        ssh_pkey=ssh_password,
        remote_bind_address=('127.0.0.1', 3306)
    )

    sshTunne

    tunnel.start()