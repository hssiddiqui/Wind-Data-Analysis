import h5py
f = h5py.File('wtk_2007.h5', 'r')
list(f.keys())
dset = f['power']
dset.shape
dset.dtype
dset[:,0]


#using site ids to generate 
wind_attributes = pd.read_csv('wind_3tier_site_metadata.csv', header = 0)
wind_capacity_factor = wind_attributes['capacity_factor']
site_ids = wind_attributes['site_id']

sample_site_ids=[113177,113178,113244,113302,113363,113420]

#hdf data processing
sum=0;

for i in range(sample_site_ids):
    sum+=dset[:,index[sample_site_ids[]]]
