[[!meta title="Web hosting"]]


All accounts include hosting with a web address at:

* **`https://www.ocf.berkeley.edu/~user`** (canonical version)
* **`https://ocf.io/user`** (shorter version)

where `user` is the account name.

Groups, faculty, and staff may also request a [[virtual host|doc
services/vhost]] for another domain (e.g., group.berkeley.edu).

## Uploading Files    {upload}

Upload files to your web space the same way you [[upload files to your OCF
account|doc services/shell]] (typically SFTP if used remotely). The only
difference is that files for your web space are placed in your `public_html`
directory.

## Additional details

The web server runs Apache 2.4 with FastCGI (mod_fcgid), suEXEC, and suPHP.
Access and error logs are accessible in `/opt/httpd` using [[SSH|doc
services/shell]].

The web server itself runs as a dedicated user. If your .htaccess file is not
world-readable (e.g., `chmod 644`), the web server will return the error "401
Forbidden".

PHP/CGI/FastCGI scripts are executed as your user, so they do not need to be
world-readable. If they contain sensitive information (such as database
passwords), you should make them private (e.g., `chmod 600` or `chmod 700`).

Both individual hosting and student group hosting are done entirely over HTTPS.


### Supported languages     {languages}

* PHP 5.6
* Perl 5.20.2
* Python 2.7, and 3.4; Django 1.7.7; Flask 0.10.1
* Ruby 2.1.5; Rails 4.1.8

Other flavors of the day may work but are not currently supported. We may be
able to install additional packages on request, but will generally advise you
to use alternatives instead (such as installing in a virtualenv or inside your
home directory).


## FAQ    {faq}

### My `public_html` directory is missing, how do I fix that?

We automatically create the `public_html` symlink for all new accounts, but
it's possible that it was accidentally removed (or that you have an older
account from before we started the practice).

Keep in mind that just recreating the directory is *not* sufficient; it must be
a symbolic link to your actual web space. If you simply make a directory named
`public_html`, it won't be used for your website.

Here are two easy ways to re-create the symlink:


#### via the web interface

1. Open the [[web commands interface|commands]] in your web browser.
2. Select the "makehttp" option. Enter your OCF username and password, and
   choose "Run command". You should see something like this in the output,
   assuming you entered your username and password correctly:

        public_html folder has been created successfully.


#### via SSH    {ssh}

1. Login to your account via [[SSH|doc services/shell]].
2. After you go past all system messages, you will see prompt:

        tsunami$

    At this prompt, type `makehttp`. This command will create your web
    directory. Here's a sample screen output:

        tsunami$ makehttp
        public_html folder has been created successfully.
