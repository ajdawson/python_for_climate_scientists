import cis
import numpy as np

files = ["../resources/WorkshopData2016/AerosolCCI/20080411002335-ESACCI-L2P_AEROSOL-AER_PRODUCTS-AATSR-ENVISAT-ORAC_31962-fv03.04.nc",
         "../resources/WorkshopData2016/AerosolCCI/20080411020411-ESACCI-L2P_AEROSOL-AER_PRODUCTS-AATSR-ENVISAT-ORAC_31963-fv03.04.nc",
         "../resources/WorkshopData2016/AerosolCCI/20080411034447-ESACCI-L2P_AEROSOL-AER_PRODUCTS-AATSR-ENVISAT-ORAC_31964-fv03.04.nc",
         "../resources/WorkshopData2016/AerosolCCI/20080411052523-ESACCI-L2P_AEROSOL-AER_PRODUCTS-AATSR-ENVISAT-ORAC_31965-fv03.04.nc",
         "../resources/WorkshopData2016/AerosolCCI/20080411070559-ESACCI-L2P_AEROSOL-AER_PRODUCTS-AATSR-ENVISAT-ORAC_31966-fv03.04.nc"]


def subset_africa(ungridded_data):
    northern_africa_lat_bounds = -20, 50
    northern_africa_lon_bounds = 0, 40
    southern_africa_lat_bounds = 10, 50
    southern_africa_lon_bounds = -40, 0
    africa_points = np.zeros_like(ungridded_data.data)
    for i, d in enumerate(ungridded_data.data):
        if ((northern_africa_lat_bounds[0] < ungridded_data.lat[i] < northern_africa_lat_bounds[1]) and
            (northern_africa_lon_bounds[0] < ungridded_data.lon[i] < northern_africa_lon_bounds[1])) or \
            ((southern_africa_lat_bounds[0] < ungridded_data.lat[i] < southern_africa_lat_bounds[1]) and
             (southern_africa_lon_bounds[0] < ungridded_data.lon[i] < southern_africa_lon_bounds[1])):
            africa_points[i] = 1
    return ungridded_data[africa_points]


def subset_aerosol_cci_over_africa():
    from cis.data_io.ungridded_data import UngriddedDataList
    subsetted_data = UngriddedDataList()
    for f in files:
        d = cis.read_data(f, "AOD550")
        subsetted_data.append(subset_africa(d))
    return subsetted_data


if __name__ == '__main__':
    subset = subset_aerosol_cci_over_africa()
    subset.plot()