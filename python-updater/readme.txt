NCL Functions and Resources Updater for Sublime Text 3
@author: zamlty
@version: 2017.08.14

- functions
    url: http://www.ncl.ucar.edu/Document/Functions/list_alpha.shtml
    num: 1394

- resources
    url: http://www.ncl.ucar.edu/Document/Graphics/Resources/list_alpha_res.shtml
    num: 1486

- color tables
    url: http://www.ncl.ucar.edu/Document/Graphics/color_table_gallery.shtml
    num: 241

- keywords
    url: http://www.ncl.ucar.edu/Document/Manuals/Ref_Manual/NclKeywords.shtml
    num: 52

- named colors
    url: http://www.ncl.ucar.edu/Applications/Scripts/rgb.txt
    num: 752

- function completions
    url: http://www.ncl.ucar.edu/Document/Functions/list_alpha.shtml
    num: 1394
    unmatched: [
        dsgrid3d, dspnt2d, dspnt2s, dspnt3d, dspnt3s, extract_globalatts_hdf5,
        gsn_add_shapefile_polygons, gsn_csm_vector_scalar_map_polar,
        parse_globalatts_hdf5, stdMonTLLL, str_match_ind_ic_regex, ushorttoint
    ]
    typo: [
        { "trigger": "extract_globalatts_hdf5", "contents": "extract_globalatts_hdf5(${1:hinfo}, ${2:name_to_extract})" },
    ]
