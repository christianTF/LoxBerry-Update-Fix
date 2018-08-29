#!/usr/bin/perl

use LoxBerry::Web;
my $plugintitle = "LoxBerry Update FIX V" . LoxBerry::System::pluginversion();
#my $helplink = "https://www.loxwiki.eu/x/-gA_Ag";
#my $helptemplate = "help.html";

LoxBerry::Web::lbheader($plugintitle, $helplink, $helptemplate);

my $template = HTML::Template->new(
    filename => "$lbptemplatedir/index.html",
    global_vars => 1,
    loop_context_vars => 1,
    die_on_bad_params => 0,
);

print $template->output();

LoxBerry::Web::lbfooter();
