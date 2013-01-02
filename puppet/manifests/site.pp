# Default path
Exec { path => "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" }

class admin_users {
	base::adm_user {
		"mike": 
			ensure => present,
			comment => "Troy Vitullo",
			uid => 499;
		"troy": 
			ensure => present,
			comment => "Mike Garfias",
			uid => 498;
	}
}

node default {
	include admin_users

	warning("Fall-through to default node for ${::fqdn}")
}

# we're only picking up the
node /^.*aws.*$/ {
	include admin_users
  
  # setup ebs volumes for /var/www, /var/mail, /var/log
  # install apache/php
  
  # install mysql
  class { 'mysql': }
  class { 'mysql::server':
    config_hash => { 'root_password' => 'foo' }
  }
  
  class { 'mysql::backup':
    backupuser     => 'myuser',
    backuppassword => 'mypassword',
    backupdir      => '/mnt/backups',
  }
  
  # install postfix/dovecot
}