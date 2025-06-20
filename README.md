[![Anaconda-Server Badge](https://anaconda.org/conda-forge/jsongrapher/badges/version.svg)](https://anaconda.org/conda-forge/jsongrapher) [![Anaconda-Server Badge](https://badge.fury.io/py/jsongrapher.svg)](https://badge.fury.io/py/jsongrapher)

# JSONGrapher (python)

Imagine a world where a person can simply drag a data file into a graphing utility and a plot will be made -- including axes with the data's units. Imagine that data from data other sources (with other units) can then be dragged in for comparison, with all data plotted on an interactive graph. Imagine that the units of all of these datasets will be converted automatically, as needed, during the plotting.

Create interactive plots just by drag-and-drop of JSON records. Share the json files for easy plotting by others. JSONGrapher will automatically convert units between records to plot the data sets together, to enable comparisons. For example, if one record is in kg/s and another in g/s, JSONGrapher will do the conversion automatically to plot both records together, for comparison. Tools and examples are included for how to create JSON records.

To use python JSONGrapher, first install it using conda or pip:<br>
`pip install JSONGrapher[COMPLETE]` or `conda install conda-forge::jsongrapher` <br>
Alternatively, you can download the directory directly.<br> 

## **0\. Plotting a JSON Record**
To create an interactive plot, you just need one line of code! <br>
Then drag an [example](https://github.com/AdityaSavara/jsongrapher-py/tree/main/examples/example_1_drag_and_drop) JSONGrapher record into the window to plot! Below are example 2D and 3D plots. <br>
Further below shows how easy it is to create your own json records.
<pre>
import JSONGrapher; JSONGrapher.launch()
# Then just drag records into the window!
</pre>

<a href="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_1_drag_and_drop/images/JSONGrapherWindowShortened.gif"><img src="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_1_drag_and_drop/images/JSONGrapherWindowShortened.gif" width="20%"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
<a href="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_1_drag_and_drop/images/UAN_DTA_image.gif"><img src="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_1_drag_and_drop/images/UAN_DTA_image.gif" width="25%"></a>
<br>
<a href="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_1_drag_and_drop/images/Rate_Constant_mesh3d.gif"><img src="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_1_drag_and_drop/images/Rate_Constant_mesh3d.gif" width="35%"></a>
<a href="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_1_drag_and_drop/images/Rate_Constant_Scatter3d_example10.gif"><img src="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_1_drag_and_drop/images/Rate_Constant_Scatter3d_example10.gif" width="35%"></a>
<br>
<a href="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_1_drag_and_drop/images/Rate_Constant_bubble.gif"><img src="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_1_drag_and_drop/images/Rate_Constant_bubble.gif" width="35%"></a>&nbsp;&nbsp;&nbsp;
<a href="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_1_drag_and_drop/images/SrTiO3_rainbow_image.gif"><img src="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_1_drag_and_drop/images/SrTiO3_rainbow_image.gif" width="30%"></a>
<br><br>
<a href="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_1_drag_and_drop/images/O_OH_Scaling.gif"><img src="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_1_drag_and_drop/images/O_OH_Scaling.gif" width="50%"></a>


## **1\. Preparing to Create a Record**

The remainder of this landing page follows a json record tutorial [example file](https://github.com/AdityaSavara/jsongrapher-py/blob/main/examples/example_2_creating_records_and_using_styles/example_2_json_record_tutorial.py) which shows how to create graphable .json records. The records can then be plotted with python JSONGrapher or with jsongrapher.com<br>

Let's create an example where we plot the height of a pear tree over several years. 
<pre>
Record = JSONRecordCreator.create_new_JSONGrapherRecord()
x_label_including_units = "Time (years)"
y_label_including_units = "Height (m)"
time_in_years = [0, 1, 2, 3, 4]
tree_heights = [0, 0.42, 0.86, 1.19, 1.45]
</pre>

## **2\. Populating the New JSONGrapher Record**

<pre>
Record.set_comments("Tree Growth Data collected from the US National Arboretum")
Record.set_datatype("Tree_Growth_Curve")
Record.set_x_axis_label_including_units(x_label_including_units)
Record.set_y_axis_label_including_units(y_label_including_units)
Record.add_data_series(series_name="pear tree growth", x_values=time_in_years, y_values=tree_heights, plot_type="scatter_spline")
Record.set_graph_title("Pear Tree Growth Versus Time")
</pre>

## **3\. Exporting to File**

We can export a record to a .json file, which can then be used with JSONGrapher. 
<pre>
Record.export_to_json_file("ExampleFromTutorial.json")
Record.print_to_inspect()
</pre>

<p><strong>Expected Output:</strong></p>
<pre>
JSONGrapher Record exported to, ./ExampleFromTutorial.json
{
    "comments": "Tree Growth Data collected from the US National Arboretum",
    "datatype": "Tree_Growth_Curve",
    "data": [
        {
            "name": "pear tree growth",
            "x": [0, 1, 2, 3, 4],
            "y": [0, 0.42, 0.86, 1.19, 1.45],
            "type": "scatter",
            "line": { "shape": "spline" }
        }
    ],
    "layout": {
        "title": "Pear Tree Growth Versus Time",
        "xaxis": { "title": "Time (year)" },
        "yaxis": { "title": "Height (m)" }
    }
}
</pre>

## **4\. Plotting to Inspect**

We can plot the data with plotly, interact with the graph, and save as a png file.
<pre>
Record.plot_with_plotly() #Try hovering your mouse over points after this command!
</pre>
<a href="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_2_creating_records_and_using_styles/image_from_tutorial_plotly_fig.png"><img src="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_2_creating_records_and_using_styles/image_from_tutorial_plotly_fig.png" width="40%"></a>

We can plot the data using Matplotlib and export the plot as a PNG file.
<pre>
Record.plot_with_matplotlib()
Record.export_to_matplotlib_png("image_from_tutorial_matplotlib_fig")
</pre>
<a href="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_2_creating_records_and_using_styles/image_from_tutorial_matplotlib_fig.png"><img src="https://raw.githubusercontent.com/AdityaSavara/JSONGrapher-py/main/examples/example_2_creating_records_and_using_styles/image_from_tutorial_matplotlib_fig.png" width="40%"></a>

You can also see more examples: https://github.com/AdityaSavara/jsongrapher-py/tree/main/examples

Additionally, json records you send to others can be plotted by them at www.jsongrapher.com
This 'see the plot using a browser' capability is intended to facilitate including JSONGrapher records in supporting information of scientific publications.


## **Contributing to JSONGrapher, Feature Suggestions, and Reporting Issues**

These interactions should be through github at https://github.com/AdityaSavara/jsongrapher-py

To contribute to JSONGrapher, make a pull request with sufficient details about what issue you are trying to solve, and adequate commenting in your code to follow the logic. After that, be prepared for further communication if needed.

To suggest features, create a new issue under the issues tab.

To report issues, create a new issue under the issues tab.
