import pandas as pd

class Reader:

    def __init__(self):
        pass

    def line_to_values(self, line:str, sep: str=';')-> list:
        """
        a function that split a line on 'sep' 
        """
        # remove trailing spaces
        line = line.strip('\n').strip(' ')

        # split the line into seperate records
        values = [value.strip(' ') for value in line.split(sep) if value]

        return values

    def read_data(self, data_file: str, sep: str=';', n_veh: int=4, n_traj: int=6):
        """
        a function that reads a csv file and extract:
        - columns : names of columns
        - vehicles: vehicle data in the first n_veh=4 columns
        - trajectories: trajectory data in the remaining columns, repeated every n_traj=6 columns
        """
        
        vehicles = []
        trajectories = []

        with open(data_file, 'r') as file:
            lines = file.readlines()

            # first line contains columns names
            columns = self.line_to_values(lines[0], sep=sep)
            lines = lines[1:]
            if (len(columns)!= n_veh+n_traj):
                raise ValueError(f"Column names do not match the values {n_veh} + {n_traj}")

            for indx, line in enumerate(lines):
                values = self.line_to_values(line, sep= sep)

                # first n_veh values are vehicle data and the rest are trajectory data
                vehicles.append(values[:n_veh])

                traj = values[n_veh:] 
                stamps = int(len(traj)/n_traj) #number of timestamps

                try:
                    assert(len(traj)%n_traj == 0)
                    # insert trajectory data  
                    trajectories = trajectories + [values[:1] + traj[n_traj*i: n_traj*(i+1)] for i in range(stamps)]
                except:
                    print(f"Error in reading trajectory data at line {indx}")
                    continue
        
        return columns, vehicles, trajectories

    def data_dfs(self, data_file: str, sep: str=';', n_veh: int=4, n_traj: int=6):
        """
        a function that reads a csv file into 2 pd.DataFrames:
        - df_vehicles: vehicle data in the first n_veh=4 columns
        - df_trajectories: trajectory data in the remaining columns, repeated every n_traj=6 columns
        """

        columns, vehicles, trajectories = self.read_data(data_file, sep, n_veh, n_traj)

        cols_veh = columns[:n_veh]
        cols_traj = columns[:1] + columns[n_veh:]

        df_vehicles = pd.DataFrame(data= vehicles, columns= cols_veh)
        df_trajectories = pd.DataFrame(data= trajectories, columns= cols_traj)

        return df_vehicles, df_trajectories