Name:           translate-shell
Version:        0.9.6.12
Release:        1
License:        Public Domain
Summary:        Command-line translator using Google Translate, Bing Translator, Yandex.Translate, etc.
Group:          Text tools
Url:            http://www.soimort.org/translate-shell
Source0:        https://github.com/soimort/translate-shell/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  gawk >= 4.0
Requires:       gawk >= 4.0
Recommends:     fribidi
Recommends:     mplayer
Recommends:     rlwrap
Recommends:     groff
Recommends:     curl

%description
Translate Shell is a command-line interface and interactive shell
for Google Translate, Bing Translator, Yandex Translate etc.
It works just the way you want it to be.

Translate Shell is a complete rewrite of Google Translate CLI Legacy,
which is a tiny script written in 100 lines of AWK code.
Translate Shell is backward compatible with Google Translate CLI Legacy
in its command-line usage; furthermore, it provides more functionality
including verbose translation, Text-to-Speech and interactive mode, etc.

Run <man trans> in the terminal for usage information.

%prep
%setup -q

%build
%make_build

%install
install -pd %{buildroot}%{_bindir}
install -pd %{buildroot}%{_mandir}/man1
install -pm0755 build/trans %{buildroot}%{_bindir}
install -pm0644 man/trans.1 %{buildroot}%{_mandir}/man1

%files
%doc LICENSE README.md WAIVER CONTRIBUTING.md
%{_bindir}/trans
%{_mandir}/*/*
