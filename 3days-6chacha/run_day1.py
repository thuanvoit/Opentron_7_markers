#
# MASTER PROTOCOL FOR 6 CHACHA SLIDES = 24 SLIDES
#
from opentrons import protocol_api
#
# Chacha 1 + 2 + 3 are connected
# Chacha 4 + 5 + 6 are connected
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
chacha_location = {
    # chacha1
    1: {"active": False,
        "position": 1,
        "slides": {1: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                            'rows': ['G', 'H']}},
                   2: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}},
                   3: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}},
                   4: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}}, }
        },
    # chacha2
    2: {"active": True,
        "position": 2,
        "slides": {1: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                            'rows': ['G', 'H']}},
                   2: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}},
                   3: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}},
                   4: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}}, }
        },
    # chacha3
    3: {"active": True,
        "position": 3,
        "slides": {1: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                            'rows': ['G', 'H']}},
                   2: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}},
                   3: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}},
                   4: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}}, }
        },
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # chacha4
    4: {"active": True,
        "position": 1,
        "slides": {1: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                            'rows': ['G', 'H']}},
                   2: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}},
                   3: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}},
                   4: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}}, }
        },
    # chacha5
    5: {"active": False,
        "position": 2,
        "slides": {1: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                            'rows': ['G', 'H']}},
                   2: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}},
                   3: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}},
                   4: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}}, }
        },
    # chacha6
    6: {"active": False,
        "position": 3,
        "slides": {1: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                            'rows': ['G', 'H']}},
                   2: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}},
                   3: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}},
                   4: {"active": True, "workRegion": {'cols': ['2', '3'],
                                                           'rows': ['G', 'H']}}, }
        },
}
# Define other labwares
tiprack_location = 7
tuberack_15_location = 8
tbst_well_location = 9
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Start protocols
def antibody_def(tuberack, tbst_well=None):
    tbst_well = {
        "tbst": {"position": "A1", "volume": 250, "time": {"mins": 1, "sec": 0}, "labware": tbst_well, "used": 0},
    }
    solution_in_tuberack = {
        # 1st ROW ~~~~~~~~~~~~~~~~~~~~~#
        # 1st RUN ~~~~~~~~~~~~~~~~~~~~~#
        "opal_antibody_dilluent": {"position": "A1", "volume": 250, "time": {"mins": 10, "sec": 0}},
        "cd8": {"position": "A2", "volume": 250, "time": {"mins": 30, "sec": 0}},
        "opal_polymer_HRP": {"position": "A3", "volume": 250, "time": {"mins": 10, "sec": 0}},
        "opal_690_fluorophore": {"position": "A4", "volume": 250, "time": {"mins": 10, "sec": 0}},
        # 2nd RUN ~~~~~~~~~~~~~~~~~~~~~#
        "foxp3": {"position": "A5", "volume": 250, "time": {"mins": 60, "sec": 0}},

        # 2nd ROW ~~~~~~~~~~~~~~~~~~~~~#
        "opal_620_fluorophore": {"position": "B1", "volume": 250, "time": {"mins": 10, "sec": 0}},
        "empty": {"position": "B2", "volume": 0, "time": {"mins": 0, "sec": 0}},
        "empty": {"position": "B3", "volume": 0, "time": {"mins": 0, "sec": 0}},
        "empty": {"position": "A4", "volume": 0, "time": {"mins": 0, "sec": 0}},
        "empty": {"position": "B5", "volume": 0, "time": {"mins": 0, "sec": 0}},
        # 3rd ROW ~~~~~~~~~~~~~~~~~~~~~#
        "empty": {"position": "C1", "volume": 0, "time": {"mins": 0, "sec": 0}},
        "empty": {"position": "C2", "volume": 0, "time": {"mins": 0, "sec": 0}},
        "empty": {"position": "C3", "volume": 0, "time": {"mins": 0, "sec": 0}},
        "empty": {"position": "C4", "volume": 0, "time": {"mins": 0, "sec": 0}},
        "empty": {"position": "C5", "volume": 0, "time": {"mins": 0, "sec": 0}},
    }

    # Add labware to each solution
    for sol in solution_in_tuberack:
        solution_in_tuberack[sol]["labware"] = tuberack
        solution_in_tuberack[sol]["used"] = 0

    # Add TBST Well to Solution List if using
    if tbst_well != None:
        solution_in_tuberack.update(tbst_well)
    return solution_in_tuberack

~~~~~~~~~~~~~~~~~~~~~#
class Opentron_Chacha:
    tip_count = 0

    def __init__(self, protocol, pipette, chacha_group, location, working_row, antibody_solution):
        self.protocol = protocol
        self.pipette = pipette
        self.chacha_group = chacha_group
        self.location = location
        self.working_row = working_row
        self.antibody_solution = antibody_solution
        self.warm_up()
        
    
    def warm_up(self):
        self.light_off(True)
        self.comment("Protocol start after 5 seconds")
        self.protocol.delay(seconds=5)
        self.comment("Protocol starts")
    
    def light_off(self, is_off):
        if is_off:
            self.comment("Light off, protocol will start soon!")
            self.protocol.set_rail_lights(False)
        else:
            self.comment("Light on, protocol are done!")
            self.protocol.set_rail_lights(True)

    
    def comment(self, msg):
        new_msg = f"> !!! > {msg} < !!! <"
        n=len(new_msg)
        self.protocol.comment("")
        self.protocol.comment("")
        self.protocol.comment("~"*n)
        self.protocol.comment(new_msg)
        self.protocol.comment("~"*n)
        self.protocol.comment("")

        
    # remove all unactive slides
    def active_slide_chacha(self, location):
        for i in range(len(location)):
            if not location[i+1]["slides"][1]["active"]: del location[i+1]["slides"][1]
            if not location[i+1]["slides"][2]["active"]: del location[i+1]["slides"][2]
            if not location[i+1]["slides"][3]["active"]: del location[i+1]["slides"][3]
            if not location[i+1]["slides"][4]["active"]: del location[i+1]["slides"][4]
        return location

    # WASH OFF LIQUIDS
    def washing(self, time=3):

        self.comment(f"Wash row {self.working_row}")
        for i in range(time):

            #drain
            for row in self.working_row:
                chacha_n = 0
                if row == 1: 
                    if 1 in self.chacha_group:
                        chacha_labware = self.get_chacha(1)
                        chacha_n = 1
                    elif 2 in self.chacha_group:
                        chacha_labware = self.get_chacha(2)
                        chacha_n = 2
                    elif 3 in self.chacha_group:
                        chacha_labware = self.get_chacha(3)
                        chacha_n = 3
                    else: break
                elif row == 2:
                    if 4 in self.chacha_group:
                        chacha_labware = self.get_chacha(4)
                        chacha_n = 4
                    elif 5 in self.chacha_group:
                        chacha_labware = self.get_chacha(5)
                        chacha_n = 5
                    elif 6 in self.chacha_group:
                        chacha_labware = self.get_chacha(6)
                        chacha_n = 6
                    else: break
                else: break
                self.comment(f"Start washing row #{row} using chacha #{chacha_n}")

                self.pipette.move_to(chacha_labware['A6'].top(20))
                self.pipette.move_to(chacha_labware['A6'].top(-10), speed=150)
                self.pipette.move_to(chacha_labware['A6'].top(-5))
                self.pipette.move_to(chacha_labware['A6'].top(-10), speed=150)
            
            #wait
            self.protocol.delay(seconds=2)

            #original position
            for row in self.working_row:
                if row == 1: 
                    if 1 in self.chacha_group:
                        chacha_labware = self.get_chacha(1)
                    elif 2 in self.chacha_group:
                        chacha_labware = self.get_chacha(2)
                    elif 3 in self.chacha_group:
                        chacha_labware = self.get_chacha(3)
                elif row == 2:
                    if 4 in self.chacha_group:
                        chacha_labware = self.get_chacha(4)
                    elif 5 in self.chacha_group:
                        chacha_labware = self.get_chacha(5)
                    elif 6 in self.chacha_group:
                        chacha_labware = self.get_chacha(6)
                else: break
                self.pipette.move_to(chacha_labware['L6'].top(20))
                self.pipette.move_to(chacha_labware['L6'].top(5), speed=150)
                self.pipette.move_to(chacha_labware['O6'].top(5), speed=150)
                self.pipette.move_to(chacha_labware['O6'].top(-1), speed=100)

    def get_location(self, antibody_type):
        if antibody_type in self.antibody_solution.keys():
            position = self.antibody_solution[antibody_type]['position']
            return position
        else:
            self.protocol.pause(
                f"ERROR: Something wrong with '{antibody_type}'")
            return None

    def get_volume(self, antibody_type):
        if antibody_type in self.antibody_solution.keys():
            volume = self.antibody_solution[antibody_type]['volume']
            return volume
        else:
            self.protocol.pause(
                f"ERROR: Something wrong with '{antibody_type}'")
            return None

    def get_time(self, antibody_type):
        if antibody_type in self.antibody_solution.keys():
            time = [self.antibody_solution[antibody_type]['time']['mins'],
                    self.antibody_solution[antibody_type]['time']['sec']]
            return time
        else:
            self.protocol.pause(
                f"ERROR: Something wrong with '{antibody_type}'")
            return None

    def get_labware(self, antibody_type):
        if antibody_type in self.antibody_solution.keys():
            labware = self.antibody_solution[antibody_type]['labware']
            return labware
        else:
            self.protocol.pause(
                f"ERROR: '{antibody_type}' is not one of antibody_solution defined")
            return None

    def volume_used(self, antibody_type, volume_used):
        current_volume_used = self.antibody_solution[antibody_type]['used']
        current_volume_used += volume_used
        self.antibody_solution[antibody_type]['used'] = current_volume_used

    def material_report(self):
        self.comment(f'TOTAL VOLUME REPORT')
        for antibody in self.antibody_solution:
            if antibody != "empty":
                solution = self.antibody_solution[antibody]
                volume_used = solution['used']
                self.protocol.comment(
                    f'Total Volume {antibody} used is {volume_used}uL ~ {str(volume_used/1000)}mL')
        self.protocol.comment(f'Total Tip Used: {self.tip_count}')

    def mix(self, volume, location, n_time=2):
        self.comment(f"Mix solution {n_time} times")
        for n in range(n_time):
            self.pipette.aspirate(volume, location)
            self.pipette.dispense(volume, location)

    def volume_this_block(self, block, antibody_type):
        count = 0
        for i in self.location[block]["slides"]:
            count+=1
        return count * self.antibody_solution[antibody_type]["volume"]
    
    def get_total_slide(self, row):
        count = 0
        if row == 1 or row == "1": rows = [1,2,3]
        elif row == 2 or row == "2": rows = [4,5,6]
        else: pass
        for e in rows:
            if e in self.location:
                for slide in self.location[e]["slides"]:
                    count+=1
            else: pass
        return count
    
    def get_total_volume_row(self, row, antibody_type):
        volume_each_slide = self.get_volume(antibody_type)
        return self.get_total_slide(row) * volume_each_slide

    def get_workRegion_cols(self, slide):
        return slide["workRegion"]["cols"]
    
    def get_workRegion_rows(self, slide):
        return slide["workRegion"]["rows"]

    # get chacha position
    def get_chacha(self, location):
        # self.comment(self.group[int(chacha)])
        return self.chacha_group[int(location)]

    # blocking method
    def pipette_1000(self, antibody_type, group_row, to_wait=True):
        self.tip_count += 1 #count +1 tip

        antibody_position = self.get_location(antibody_type)
        antibody_volume = self.get_volume(antibody_type)
        antibody_time = self.get_time(antibody_type)
        antibody_labware = self.get_labware(antibody_type)

        #calculate
        max_volume_row = self.get_total_volume_row(group_row, antibody_type)
        max_volume_pipette = self.pipette.max_volume
        volume_done = 0

        if group_row == 1 or group_row == "1": group_rows = [1,2,3]
        elif group_row == 2 or group_row == "2": group_rows = [4,5,6]
        else: pass

        for block in group_rows:
            if block in self.location:
                #chacha labware
                chacha_labware = self.get_chacha(block)
                #if block is available, calculate total volume need for this block
                volume_this_block = self.volume_this_block(block, antibody_type)

                # mix up
                self.mix(max_volume_pipette, antibody_labware[antibody_position])
                
                # aspirate
                self.pipette.aspirate(volume_this_block, antibody_labware[antibody_position])
                
                #report
                self.volume_used(antibody_type, volume_this_block)

                self.comment(f"Go to block #{block} row #{group_row}")

                self.pipette.move_to(antibody_labware[antibody_position].top(20), speed=100)  # move slowly up

                for slide in self.location[block]["slides"]:
                    self.comment(f"Work with slide #{slide} of block #{block}")
                    each_slide = self.location[block]["slides"][slide]
                    cols = self.get_workRegion_cols(each_slide)
                    rows = self.get_workRegion_rows(each_slide)
                    for row in rows:
                        for col in cols:
                            self.pipette.dispense(volume_this_block/10, chacha_labware[f"{row}{col}"].top())
            else:
                self.comment(f"Block #{block} row #{group_row} is not installed or not available.")
        # wait for continue to work on different row
        if to_wait: # yes wait
            # GO TO WAITING POSITION
            self.comment(f"Start waiting for {antibody_time[0]} min, {antibody_time[1]} sec")
            self.protocol.delay(minutes=antibody_time[0], seconds=antibody_time[1])

    # 2 rows at the same time
    # 2 rows max
    def pipette_1000_master(self, antibody_type):
        if len(self.working_row) > 0 and len(self.working_row) < 3:
            self.pipette_1000(antibody_type, self.working_row[0], to_wait=False)
            self.pipette_1000(antibody_type, self.working_row[1], to_wait=True)

    # NEW RINSING
    # new name ? wash
    def rinsing_with(self, antibody_type, n_time, n_each, delay_min_in_btw, delay_sec_in_btw, mixing=False):
        position = self.get_position(antibody_type)
        volume = self.get_volume(antibody_type)

        sol_labware = self.get_labware(antibody_type)

        self.pipette.pick_up_tip()
        self.tip_count += 1

        for n in range(n_time):
            self.comment(f'WASH WITH {antibody_type} {n+1} time')
            # Washing TBST 4 times (30 seconds * 4 = 2 mins)
            for j in range(n_each):

                max_vol_4_slides = self.get_max_volume_need(antibody_type)
                max_vol_pipette = self.pipette.max_volume

                volume_to_do = 0

                while(max_vol_4_slides > 0):

                    if max_vol_4_slides <= max_vol_pipette:
                        volume_to_do = max_vol_4_slides
                    else:
                        volume_to_do = max_vol_pipette

                    if mixing:
                        self.mix_up_n_down(
                            max_vol_pipette, sol_labware[position], 3)
                    else:
                        pass

                    self.pipette.aspirate(volume_to_do, sol_labware[position])
                    self.volume_used(antibody_type, volume_to_do)

                    self.pipette.move_to(sol_labware[position].top(
                        20), speed=50)  # move slowly up

                    for i in range(self.slides_num):
                        for col in self.blocking_position[f'slide{i+1}']['cols']:
                            for row in self.blocking_position[f'slide{i+1}']['rows']:
                                self.pipette.dispense(
                                    volume/4, location=self.chacha_labware[row+col].top(5))

                    last_row_pos = self.blocking_position[f'slide{i+1}']['rows'][-1]
                    last_col_pos = self.blocking_position[f'slide{i+1}']['cols'][-1]
                    last_drop_position = self.chacha_labware[last_row_pos+last_col_pos]
                    self.pipette.blow_out(location=last_drop_position.top(5))

                    max_vol_4_slides -= volume_to_do

                self.comment(
                    f'DELAY {delay_min_in_btw} min, {delay_sec_in_btw} sec')
                self.pipette.home()
                self.protocol.delay(minutes=delay_min_in_btw,
                                    seconds=delay_sec_in_btw)
                self.washing(1)

            self.washing()

        # Remove TBST Tip
        self.pipette.drop_tip()


# Protocol Information
metadata = {
    'protocolName': "Opal 7 markers - 24 slides MAX",
    'author': "thuanvo",
    'description': "MASTER CHACHA",
    'apiLevel': "2.10"
}

def add_unique_to_list(e, lst):
    if e not in lst:
        lst.append(e)
    return lst

def run(protocol: protocol_api.ProtocolContext):

    # Turn off raillights
    protocol.set_rail_lights(False)

    # Introduce tiprack 1000uL and pipette 1000uL
    tiprack = protocol.load_labware(
        'opentrons_96_tiprack_1000ul', location=tiprack_location)
    pipette = protocol.load_instrument(
        'p1000_single', 'right', tip_racks=[tiprack])

    # Introduce Chacha labware & Tuberack & TBST Well (optional)
    custom_chacha_code = 'kissicklabdesign_384_wellplate_80ul'
    tuberack_15_code = 'opentrons_15_tuberack_falcon_15ml_conical'
    custom_tbst_well_code = 'kissicklabdesign_1_reservoir_100000ul'

    chacha_group = {}
    working_row = []

    if 1 in chacha_location and chacha_location[1]["active"]:
        chacha_group[1] = protocol.load_labware(custom_chacha_code, chacha_location[1]["position"])
        working_row = add_unique_to_list(1, working_row)
    else:
        del chacha_location[1]
        # del chacha_group[1]
    if 2 in chacha_location and chacha_location[2]["active"]:
        chacha_group[2] = protocol.load_labware(custom_chacha_code, chacha_location[2]["position"])
        working_row = add_unique_to_list(1, working_row)
    else: 
        del chacha_location[2]
        # del chacha_group[2]
    if 3 in chacha_location and chacha_location[3]["active"]:
        chacha_group[3] = protocol.load_labware(custom_chacha_code, chacha_location[3]["position"])
        working_row = add_unique_to_list(1, working_row)
    else: 
        del chacha_location[3]
        # del chacha_group[3]
    if 4 in chacha_location and chacha_location[4]["active"]:
        chacha_group[4] = protocol.load_labware(custom_chacha_code, chacha_location[4]["position"])
        working_row = add_unique_to_list(2, working_row)
    else: 
        del chacha_location[4]
        # del chacha_group[4]
    if 5 in chacha_location and chacha_location[5]["active"]:
        chacha_group[5] = protocol.load_labware(custom_chacha_code, chacha_location[5]["position"])
        working_row = add_unique_to_list(2, working_row)
    else: 
        del chacha_location[5]
        # del chacha_group[5]
    if 6 in chacha_location and chacha_location[6]["active"]:
        chacha_group[6] = protocol.load_labware(custom_chacha_code, chacha_location[6]["position"])
        working_row = add_unique_to_list(2, working_row)
    else: 
        del chacha_location[6]
        # del chacha_group[6]

    #print(chacha_location)
    print(chacha_group)

    tuberack_15 = protocol.load_labware(tuberack_15_code, tuberack_15_location)
    tbst_well = protocol.load_labware(custom_tbst_well_code, tbst_well_location)

    # Gather all solution information
    antibody_solution = antibody_def(tuberack_15, tbst_well)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~ COMMANDS START ~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    tasks = Opentron_Chacha(protocol=protocol,
                            pipette=pipette,
                            chacha_group=chacha_group,
                            location=chacha_location,
                            working_row=working_row,
                            antibody_solution=antibody_solution)
    
    #tasks.get_total_slide(1)

#     # Check Anti_body
#     tasks.check_antibodies()

#     tasks.comment('')
#     protocol.delay(minutes=0, seconds=5)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #~~~~~~~ BLOCKING using Opal Antibody Dilluent ~~~~~~~~~~~~~~~~~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    pipette.pick_up_tip()
    tasks.pipette_1000_master("opal_antibody_dilluent")
    tasks.washing() # default 3
    pipette.drop_tip()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #~~~~~~~ PRIMARY ANTIBODY INCUBATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    pipette.pick_up_tip()
    tasks.blocking_1000('cd8')
    tasks.washing(wash_n_time=3)
    pipette.drop_tip()

    #~~~~~~~ TBST ~~~~~~~~~~~~~~~~~~~~~#
    tasks.rinsing_with(antibody_type='tbst', n_time=6, n_each=1,
                       delay_min_in_btw=0, delay_sec_in_btw=30)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #~~~~~~~ SECONDARY HRP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    pipette.pick_up_tip()
    tasks.blocking_1000('opal_polymer_HRP')
    tasks.washing(wash_n_time=3)
    pipette.drop_tip()

    #~~~~~~~ TBST ~~~~~~~~~~~~~~~~~~~~~#
    tasks.rinsing_with(antibody_type='tbst', n_time=6, n_each=1,
                       delay_min_in_btw=0, delay_sec_in_btw=30)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #~~~~~~~ OPAL 690 FLUOROPHORE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    pipette.pick_up_tip()
    tasks.blocking_1000('opal_690_fluorophore')
    tasks.washing(wash_n_time=3)
    pipette.drop_tip()

    #~~~~~~~ TBST ~~~~~~~~~~~~~~~~~~~~~#
    tasks.rinsing_with(antibody_type='tbst', n_time=6, n_each=1,
                       delay_min_in_btw=0, delay_sec_in_btw=30)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #~~~~~~~ PAUSE AND REFILL ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    protocol.pause()
    tasks.comment(
        f"PLEASE REFILL [OPAL ANTIBODY DILLUENT] INTO {antibody_solution['opal_antibody_dilluent']['labware']} - {antibody_solution['opal_antibody_dilluent']['position']}\n")
    tasks.comment(
        f"PLEASE REFILL [OPAL POLYMER HRP]       INTO {antibody_solution['opal_polymer_HRP']['labware']} - {antibody_solution['opal_polymer_HRP']['position']}\n")
    tasks.comment(
        f"PLEASE PUT    [FoxP3]                  INTO {antibody_solution['foxp3']['labware']} - {antibody_solution['foxp3']['position']}\n")
    tasks.comment(
        f"PLEASE PUT       [Opal 620]               INTO {antibody_solution['opal_620_fluorophore']['labware']} - {antibody_solution['opal_620_fluorophore']['position']}\n")

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #~~~~~~~ BLOCKING using Opal Antibody Dilluent ~~~~~~~~~~~~~~~~~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    pipette.pick_up_tip()
    tasks.blocking_1000('opal_antibody_dilluent')
    tasks.washing(3)
    pipette.drop_tip()

    pipette.pick_up_tip()
    tasks.blocking_1000('foxp3')
    tasks.washing(wash_n_time=3)
    pipette.drop_tip()

    #~~~~~~~ TBST ~~~~~~~~~~~~~~~~~~~~~#
    tasks.rinsing_with(antibody_type='tbst', n_time=6, n_each=1,
                       delay_min_in_btw=0, delay_sec_in_btw=30)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #~~~~~~~ Secondary opal_polymer_HRP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    pipette.pick_up_tip()
    tasks.blocking_1000('opal_polymer_HRP')
    tasks.washing(wash_n_time=3)
    pipette.drop_tip()

    #~~~~~~~ TBST ~~~~~~~~~~~~~~~~~~~~~#
    tasks.rinsing_with(antibody_type='tbst', n_time=6, n_each=1,
                       delay_min_in_btw=0, delay_sec_in_btw=30)

    pipette.pick_up_tip()
    tasks.blocking_1000('opal_620_fluorophore')
    tasks.washing(wash_n_time=3)
    pipette.drop_tip()

    #~~~~~~~ TBST ~~~~~~~~~~~~~~~~~~~~~#
    tasks.rinsing_with(antibody_type='tbst', n_time=6, n_each=1,
                       delay_min_in_btw=0, delay_sec_in_btw=30)


    #~~~~~~~ REPORT VOLUME ~~~~~~~~~~~~~~~~~~~~~#
    tasks.material_report()
