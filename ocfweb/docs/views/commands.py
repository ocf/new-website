from typing import NamedTuple
from typing import Optional

from django.shortcuts import render


class Command(NamedTuple):
    name: str
    args: Optional[str]
    desc: str
    doc: Optional[str] = None
    doc_anchor: Optional[str] = None


OCF_COMMANDS = [
    Command(
        'how', 'SCRIPT',
        desc='Shows the source code for a script',
    ),
    Command(
        'makehttp', None,
        desc='Puts a shortcut to your web directory in your home folder',
        doc='services/web', doc_anchor='h3_via-ssh',
    ),
    Command(
        'makemysql', None,
        desc='Generates a new random password for your database, creating the '
             'database if it does not exist',
        doc='services/mysql', doc_anchor='h3_ssh-terminal',
    ),
    Command(
        'paper', None,
        desc='Shows how many pages you can currently print',
    ),
    Command(
        'update-email', None,
        desc='Prompts you to set a contact email address for your OCF account',
    ),
]

FILE_COMMANDS = [
    Command(
        'cd', 'DIRECTORY',
        desc='Changes the current directory to a new one',
    ),
    Command(
        'cp', '[-r] SOURCE DEST',
        desc='Copies a file. The <code>-r</code> option allows for copying '
             'directories.',
    ),
    Command(
        'less', 'FILE',
        desc='Lets you view the contents of a text file',
    ),
    Command(
        'ls', '[FILE]',
        desc='Lists information about files and directories',
    ),
    Command(
        'mkdir', 'DIRECTORY',
        desc='Creates a new directory',
    ),
    Command(
        'nano', 'FILE',
        desc='Lets you edit a text file with a basic interface',
    ),
    Command(
        'mv', 'SOURCE DEST',
        desc='Moves or renames a file or folder',
    ),
    Command(
        'rm', '[-r] FILE',
        desc='Deletes a file. The <code>-r</code> option allows for deleting '
             'non-empty directories.',
    ),
    Command(
        'rmdir', 'DIRECTORY',
        desc='Deletes an empty directory. Safer than <code>rm -r</code>.',
    ),
]


def commands(doc, request):
    return render(
        request,
        'docs/commands.html',
        {
            'title': doc.title,
            'ocf_commands': OCF_COMMANDS,
            'file_commands': FILE_COMMANDS,
        },
    )
