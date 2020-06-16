---
title: "Package managers and distributions"
teaching: 180
exercises: 30
questions:
- What are the benefits of using package managers and distributions?
- How can we establish and control computation environments using
  available package managers and distributions?
- Which distribution(s) best suit my needs and use-cases?
objectives:
- Explain the differences between available distributions and package
  managers
- Teach how it is possible to (re-)create a computational environment
  given a set of requirements (packages/versions)
keypoints:
- "Package managers and distributions allow for the efficient creation of tightly version-controlled computation environments."
---

## What is a “package manager" and how does it relate to a "distribution”?

The installation and maintenance of computing environments is tedious and
error-prone if you manually download, build, test, and install each
software package from various locations on the web. Moreover,
how could you be certain that the software version you installed
today is identical to the software you installed yesterday?

To standardize and automate software delivery to users, **package managers**
wrap each software product into one (or more) packages, with all the
necessary metadata, so that they can be installed on the system via the same
package management interface regardless of the software origin, programming
language, etc.  Moreover, package managers provide detailed versioning,
dependencies, and other metadata that help guarantee the consistency and
reproducibility of a computing environment.

Software **distributions** use a manager to
index a collection of hosted packages in order to centralize delivery and
streamline installation. In this way, the same package manager platform
can be used by multiple distributions. For instance, the Debian distribution (and its
derived distributions, such as Ubuntu) uses the **APT** package manager; Anaconda
and miniconda Python-oriented distributions use the **conda** package manager, etc.

In the following lesson, we'll survey the most commonly used
neuroimaging software and data distributions, and touch on how
they help establish unambiguous and reproducible computing environments.


## Debian

Debian is the largest community-driven open source project, and one of the
oldest Linux distributions. Its platform and package format (DEB) and package
manager (APT) became very popular and Debian provides the
base for many derivatives such as Ubuntu and Mint. At the moment, Debian provides
over 40,000 binary packages for virtually any field, some of which have many scientific applications.  Any number of those packages can be easily
installed via the APT package manager with clear information
about versioning, licensing, etc. Interestingly, almost all Debian packages are
now themselves guaranteed to be reproducible
(see [Debian: Reproducible Builds](https://wiki.debian.org/ReproducibleBuilds).

Because of such variety, as well as its wide range of support for hardware, acknowledged stability,
and adherence to principles of open and free software, Debian is a very popular
"base OS" for either direct installation on hardware, or in the cloud or
containers (e.g., [Docker](https://www.docker.com/) or [Singularity](https://www.sylabs.io/singularity/)).

> ## External teaching materials
>
> Before going through the rest of this lesson, you should learn the
> basics of shell usage and scripting. The following lesson provides a
> good overview of all basic concepts.  Even if you are familiar with
> shell and shell scripting, please review the lesson and
> try to complete all exercises in it, especially if you do not readily know
> their correct answers:
>
>   - [Debian Reference: Ch.2 Debian package management (full: 1 h, review: 20 min)](https://www.debian.org/doc/manuals/debian-reference/ch02.en.html) --
>     a part of the thorough user-oriented Debian manual, the first chapter of which presents the basics of working
>     in the Linux environment, thus echoing our "Command line/shell" lesson; here we recommend
>     concentrating on package management.
{: .callout}

Debian (and its derivative) distributions typically only provide the single most recent
version of a software package. It does so by design to guarantee that all
available software in the released version of Debian work correctly together.
If multiple versions were were present (including possibly newer
versions) it would be impossible to provide such a guarantee. However, more recent versions
of the package often need to be installed. For this purpose,
[Debian backports](http://backports.debian.org) provide an APT repository for
stable releases of Debian with some package versions brought from Debian testing.
Enabling a backports APT repository makes it possible to install more recent versions of packages
on top of the stable Debian release. This way, multiple versions of the package
might be made available -- one (or even more if `/updates` suite was also added)
from Debian proper, and some newer version from backports. It is also made clear that one version
is considered stable, and that another one is possibly less tested.

One of the most useful commands to discover details about the available versions
of software (if operating just in the shell), is `apt policy`.

- `apt policy` shows information about all enabled APT repositories

- `apt policy PACKAGE` command shows installed and available version(s) of the
  `PACKAGE`.


An indispensable resource for reproducibility is the
[Debian snapshots](http://snapshots.debian.org) archive. It provides access to
the states of all aforementioned APT repositories as they were provided in the past.
This resource allows us to obtain any previous APT repository version of a package.


## NeuroDebian

The [NeuroDebian](http://neuro.debian.net) project was established to integrate
software used for research in psychology and
neuroimaging into the standard Debian distribution. The majority of the packages
maintained by the NeuroDebian team get uploaded to Debian unstable and then
propagate to Debian and Ubuntu releases.

To facilitate access to the most recent versions
of such software on Debian and its most popular
[derivative](https://wiki.debian.org/Derivatives) [Ubuntu](http://ubuntu.com),
the NeuroDebian project established its own
[APT](https://en.wikipedia.org/wiki/APT_(Debian)) repository. So, in a sense,
this repository is similar to the [Debian backports](https://backports.debian.org/)
repository, but has several differences:

a) it also supports Ubuntu releases

b) typically backport builds are uploaded to NeuroDebian as soon as they are uploaded to Debian unstable

c) it contains some packages that have not yet made it to Debian proper

To enable NeuroDebian on your standard Debian or Ubuntu machine, use
`apt-get install neurodebian` (and follow the interactive dialogue) or just follow
the instructions on http://neuro.debian.net.

If you are using [Docker](http://docker.io),
[NeuroDebian Docker images](https://hub.docker.com/_/neurodebian/) are provided for all
supported Debian and Ubuntu releases. If you are using [Singularity](http://singularity.lbl.gov), you can use `singularity pull docker://neurodebian[:RELEASE]` to get minimalistic images, or fetch the "Ultimate NeuroDebian Image" by `singularity pull shub://neurodebian/neurodebian`.

## Conda

The [conda] package manager was initially developed for use with the
[Anaconda] product, but because of its openness became used to establish
independent popular conda "channels", such as [conda-forge] and [bioconda].
The distinguishing feature of `conda` is that it doesn't require root/super-user access
for installation and management.  Although largely Python-oriented,
`conda` distributions are not limited to Python-based projects.

> ## External teaching materials
> - [Conda: Chatsheet (review: 5 min, print: 2 pages)](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
>   a concise list of the most common conda commands.
> - [Conda: Myths and Misconceptions by Jake Vanderplas (full: 20 min, review: 4 min)](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/   )
>   summarizes central features of conda and its relationship to
>   Anaconda, pip, and pypi; if you're not sure how these relate, we
>   recommend that you read the post.


## DataLad

DataLad is both a version control system (for code and data) and a
distribution, since it provides mechanisms for aggregating multiple data
"packages" so they can be found, installed, uninstalled, updated, etc.

Aggregation of multiple datasets is done via the
[git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) mechanism,
and a dataset containing other datasets is called a
[superdataset](http://docs.datalad.org/en/latest/glossary.html) in DataLad.
One such super-dataset is provided from http://datasets.datalad.org and
aggregates hundreds of neuroscience datasets over 50TB in size altogether.
To learn about DataLad, please refer to the [VCS lesson:DataLad](../02-vcs/#datalad).


[conda]: https://en.wikipedia.org/wiki/Conda_(package_manager)
[Anaconda]: https://anaconda.org
[conda-forge]: https://conda-forge.org
[bioconda]: https://bioconda.github.io
