import DatasetCreationTools
import sys

def main(usa_st, input_table, output_data_csv, output_lookup, to_gdb, source_geom, output_fc, schema):

    if usa_st == 1:
        DatasetCreationTools.ejscreen_cal(input_table, output_data_csv, output_lookup, to_gdb, source_geom, output_fc, schema)
    if usa_st == 2:
        DatasetCreationTools.ejscreenState_cal(input_table, output_data_csv, output_lookup, to_gdb, source_geom, output_fc, schema)

    print("Complete")

if __name__ == '__main__':

    #set `option` to 1 to generate national percentiles.
    #set `option` to 2 to generate state percentiles
    option = 1

    input_ejscreen_csv = "data/EJSCREEN_2023_BG_with_AS_CNMI_GU_VI.csv"

    output_ejscreen_csv = "data/EJSCREEN_Output.csv"

    output_lookuptable_xlsx = "data/lookup.xlsx"

    output_to_featureclass = True

    geometry_source_featureclass = "data/BlockGroups.gdb/BG"

    output_featureclass_name = "data/BlockGroups.gdb/EJSCREEN_Output"

    schema_csv = "data/ejscreen_schema.csv"

    if option != 1 and option != 2:
        sys.exit("`option` must have a value of either 1 or 2")
    
    if output_to_featureclass == True:
        if not geometry_source_featureclass or not output_featureclass_name or not schema_csv:
            sys.exit("If outputing to featureclass, all parameters must have a value")
    
    main(option, input_ejscreen_csv, output_ejscreen_csv, output_lookuptable_xlsx, output_to_featureclass, geometry_source_featureclass, output_featureclass_name, schema_csv)
