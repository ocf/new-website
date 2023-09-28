[[!meta title="PHP"]]

`death`, the OCF webserver, currently runs PHP 7.4 with the following
non-standard packages installed:

* [APCu](https://www.php.net/manual/en/book.apcu.php) (opcode caching)
* [BC Math](https://www.php.net/manual/en/book.bc.php) (arbitrary precision math)
* [Bzip2](https://www.php.net/manual/en/book.bzip2.php) (compression library)
* [DBA](https://www.php.net/manual/en/book.dba.php) (database connector)
* [GD](https://www.php.net/manual/en/book.image.php) (graphics library)
* [MB String](https://www.php.net/manual/en/book.mbstring.php) (string encoding)
* [Mcrypt](https://www.php.net/manual/en/book.mcrypt.php) (cryptography library)
* [MySQL](https://www.php.net/manual/en/book.mysqli.php) (database connector)
* [SQLite](https://www.php.net/manual/en/book.sqlite.php) (database connector)
* [SOAP](https://www.php.net/manual/en/book.soap.php) (messaging protocol library)
* [XML](https://www.php.net/manual/en/book.xml.php) (markup parsing library)
* [ZIP](https://www.php.net/manual/en/book.zip.php) (compression library)

For a full list of available modules, run `phpinfo()` from a PHP script.
Plase [[contact us|doc contact]] if you are missing a module that you need
installed to get your application running.

## Custom PHP settings

If the default PHP settings are problematic for your site (for example, if you
require larger than normal file uploads), you can customize the PHP settings
used by creating [a `.user.ini` file][.user.ini] inside your web root.

In order to maintain compatibility with the OCF's PHP settings, we highly
recommend *not* copying an entire `php.ini`\* or `.user.ini` file from the web
or from another server. Instead, we advise you to create an empty `.user.ini`
and add only the settings you wish to change.

Note that `.user.ini` filename should be used, as our webserver will not look
for (per-user) `php.ini` files.

### Example `.user.ini` file

The following file, located at `~/public_html/.user.ini`, is an example of a
good `.user.ini` file.

    ; raise max upload and POST sizes
    upload_max_filesize = 32M
    post_max_size = 32M

    ; raise maximum number of input variables
    max_input_vars = 20000


[.user.ini]: https://secure.php.net/manual/en/configuration.file.per-user.php

## Security

To prevent websites from being compromised, outbound HTTP requests via
either `curl_exec()` or `file_get_contents()` are blocked.
Consider using different frameworks if your website requires outbound
HTTP requests.
