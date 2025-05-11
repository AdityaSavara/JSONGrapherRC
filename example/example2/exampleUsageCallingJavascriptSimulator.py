import json
from JSONGrapherRC import JSONRecordCreator

#Testing#
import unitpy
from unitpy.utils.parsing import parse_unit

### STEP 1: USE A JSON RECORD WITH A SIMULATE FUNCTION ###
#First, we will load a JSONGrapher record from a file.
filename = r"./amino_silane_silica_LangmuirIsothermModel_343_equilibrium.json"
with open(filename, "r") as file:
    json_dict = json.load(file)

Record_with_simulate_field = JSONRecordCreator.create_new_JSONGrapherRecord()
Record_with_simulate_field.import_from_json(json_dict)

#If we print this record, we will see that there is no x,y data, but there is a simulate field with values.
Record_with_simulate_field.print_to_inspect()

#By default, the simulation will get called if we try to make plotly figure or export to json.
Record_with_simulate_field.plot_with_plotly()
print("The data has been simulated using a javascript function, with source code called from online.")

#One can change the parameters and then update the data object by forcing simulation again. Below is an example.
#Let's first copy the record we just had.
import copy
adjusted_Record_with_simulate_field = copy.deepcopy(Record_with_simulate_field)
#There is only a single data series, so it is index 0. We'll change the rate constant and sigma_max in the simulate field
adjusted_Record_with_simulate_field.fig_dict["data"][0]["simulate"]["K_eq"] = "50.3 (1/bar)"
adjusted_Record_with_simulate_field.fig_dict["data"][0]["simulate"]["sigma_max"] =  ".4267670459667 (mol/kg)"
#Don't forget to change the name of the dataseries now that we have changed the data inside of it.
adjusted_Record_with_simulate_field.fig_dict["data"][0]["name"] = "CO2 Adsorption, K_eq = 50.3 (1/bar)"

#Now call a function to force re-simulation of the data series at index 0.
adjusted_Record_with_simulate_field.simulate_data_series_by_index(data_series_index=0)
#Now plot again.
adjusted_Record_with_simulate_field.plot_with_plotly()

#Now let's plot both records together by merging them.
import JSONGrapherRC
merged_record = JSONGrapherRC.merge_JSONGrapherRecords([Record_with_simulate_field, adjusted_Record_with_simulate_field])
#plotting with plotly.
merged_record.plot_with_plotly()
#plotting with matplotlib.
merged_record.plot_with_matplotlib()



