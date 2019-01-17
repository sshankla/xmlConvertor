# xmlConvertor
This Code converts a a csv file into xml format based on sample xml provided
1.  The could should be checked out from dev branch
2.  On your local machine(laptop/desktop) create a directory of your choice ~/<myProject>/
3.  goto that directory cd ~/<myProject>/
4.  Ensure that you have git installed on your computer. To install git follow the instructions on link https://gist.github.com/derhuerst/1b15ff4652a867391f03
5.  Ensure that you have a git account
6.  Request a collaborator access to stable branch
7.  Tell the git on your local repo about yourself by using following commands:
      git config --global user.name "<Your User Name>"
      git config --global user.email "<Your Email Id>"
8.  Tell your local repo about the remote repo using the following command:
      git remote add origin https://github.com/sshankla/xmlConvertor.git
9.  Now clone the repository using the command git clone --single-branch --branch stable origin
10. This will create a directory structure:
        - myProject
              - xmlConvertor
                    - convertor
                        - convertor.py
                        - sample.data
                        - sample.xml
                        - spool.data
11. sample.xml is the template used for creating the xml of your choice
12. The script matches the data in sample.data and using the sample.xml creates xmls for all rows on sample.data (a csv file) and writes them to spool.data

