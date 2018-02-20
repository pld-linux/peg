Summary:	Parser generators
Summary(pl.UTF-8):	Generatory parserów
Name:		peg
Version:	0.1.18
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://piumarta.com/software/peg/%{name}-%{version}.tar.gz
# Source0-md5:	992fc7887afc2a8c92cdb1acb5b935e1
Patch0:		%{name}-make.patch
URL:		http://piumarta.com/software/peg/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
peg and leg are tools for generating recursive-descent parsers:
programs that perform pattern matching on text. They process a Parsing
Expression Grammar (PEG) to produce a program that recognises legal
sentences of that grammar.

%description -l pl.UTF-8
peg i leg to narzędzia do generowania rekurencyjnych parserów -
programów wykonujących dopasowywanie wzorców na tekście. Przetwarzają
gramatykę analizy wyrażeń w formacie PEG (Parsing Expression Grammar),
aby utworzyć program rozpoznający poprawne zdania w tej gramatyce.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OFLAGS="%{rpmcflags}%{!?debug: -DNDEBUG}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	ROOT=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE.txt
%attr(755,root,root) %{_bindir}/leg
%attr(755,root,root) %{_bindir}/peg
%{_mandir}/man1/peg.1*
