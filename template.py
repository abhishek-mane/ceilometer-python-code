'''
    This python file includes code for creating html file with given result from ceilometer client.
    This file only concerns about rendering output properly on html page thats it.
'''
class Template:
    @staticmethod
    def render(listOfMeters, fileName):
        fp = open(fileName, "w")
        fp.write(Template.htmlStart)
        fp.write(Template.tableStart)

        for row in listOfMeters:
            fp.write("<tr>")
            fp.write("<td>"+row['meter']+"</td>")
            fp.write("<td>"+row['unit']+"</td>")
            fp.write("<td>"+str(row['max'])+"</td>")
            fp.write("<td>"+str(row['min'])+"</td>")
            fp.write("<td>"+str(row['avg'])+"</td>")
            fp.write("<td>"+str(row['sum'])+"</td>")
            fp.write("</tr>")

        fp.write(Template.tableEnd)
        fp.write(Template.htmlEnd)
        fp.close()
        print "Checkout %s for output" % (fileName)

    htmlStart = """
                <html>
                <head>
                    <style>
                        table {
                            color: #333; /* Lighten up font color */
                            font-family: Helvetica, Arial, sans-serif; /* Nicer font */
                            border-collapse:collapse;
                            border-spacing: 0;
                        }
                        td, th { border: 1px solid #CCC; height: 30px; padding:10px; } /* Make cells a bit taller */
                        th {
                            background: #F3F3F3; /* Light grey background */
                            font-weight: bold; /* Make sure they're bold */
                        }
                        td {
                            background: #FAFAFA; /* Lighter grey background */
                            text-align: center; /* Center our text */
                        }
                    </style>
                </head>
                <body>
    """

    tableStart = """
                <table>
                    <tr>
                        <th>Meter</th>
                        <th>Unit</th>
                        <th>Maximum</th>
                        <th>Minimum </th>
                        <th>Average</th>
                        <th>Sum</th>
                    </tr>
    """

    tableEnd = """
                </table>
    """

    htmlEnd = """
                </body></html>
    """
