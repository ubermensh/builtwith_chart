# builtwith_chart

Takes a list of url's as input, produce chart with technology lookup info for each site.

## usage

put a list of sites in input_sites/list.txt, run command
```
python __init__.py
```
It will generage 2 file: raw_list.txt and table_list.txt, withd detected technologys used by domains  in list, e.g.
```
+------------------+-----------+-------------------+-----------------------+--------------+-----------------------+-----------+-------------------+-------------------+
|       site       | analytics |    web-servers    | javascript-frameworks | tag-managers | programming-languages | databases |   web-frameworks  | operating-systems |
+------------------+-----------+-------------------+-----------------------+--------------+-----------------------+-----------+-------------------+-------------------+
|    google.com    |           | Google Web Server |                       |              |                       |           |                   |                   |
|    github.com    |           |                   |                       |              |                       |           | Twitter Bootstrap |                   |
| pypi.python.org  |           |       Nginx       |       RequireJS       |              |                       |           |                   |                   |
| en.wikipedia.org |           |        HHVM       |                       |              |          PHP          |           |                   |                   |
+------------------+-----------+-------------------+-----------------------+--------------+-----------------------+-----------+-------------------+-------------------+
```

   

### Installing


pip install builtwith
pip install prettytable


End with an example of getting some data out of the system or using it for a little demo

## Built With (LOL)

* [builtwith](https://pypi.python.org/pypi/builtwith) - Detect the technology used by a website
* [PrettyTable](https://pypi.python.org/pypi/PrettyTable) - Used to generate table with results 
 
## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details


