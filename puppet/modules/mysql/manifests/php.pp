# Class: mysql::php
#
# This class installs the mysql-php libs.
#
# Parameters:
#   [*php_package_name*]  - The name of the mysql php package.
#
# Actions:
#
# Requires:
#
# Sample Usage:
#
class mysql::php (
  $package_name   = $mysql::params::java_package_name,
  $package_ensure = 'present'
) inherits mysql::params {

  package { 'mysql-connector-java':
    ensure => $package_ensure,
    name   => $package_name,
  }

}
