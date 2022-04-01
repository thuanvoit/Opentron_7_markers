#
# MASTER PROTOCOL FOR 6 CHACHA SLIDES = 24 SLIDES
#
from turtle import position
from opentrons import protocol_api
#
# Chacha 1 + 2 + 3 are connected
# Chacha 4 + 5 + 6 are connected
#
################################################################################
chacha_location = {
    # chacha1
    1: {"active": True,
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
################################################################################
    # chacha4
    4: {"active": False,
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
################################################################################
# Start protocols
def antibody_def(tuberack, tbst_well=None):
    tbst_well = {
        "tbst": {"position": "A1", "volume": 250, "time": {"mins": 1, "sec": 0}, "labware": tbst_well, "used": 0},
    }
    solution_in_tuberack = {
        # 1st ROW ##########
        # 1st RUN ##########
        "opal_antibody_dilluent": {"position": "A1", "volume": 250, "time": {"mins": 10, "sec": 0}},
        "cd8": {"position": "A2", "volume": 250, "time": {"mins": 30, "sec": 0}},
        "opal_polymer_HRP": {"position": "A3", "volume": 250, "time": {"mins": 10, "sec": 0}},
        "opal_690_fluorophore": {"position": "A4", "volume": 250, "time": {"mins": 10, "sec": 0}},
        # 2nd RUN ##########
        "foxp3": {"position": "A5", "volume": 250, "time": {"mins": 60, "sec": 0}},

        # 2nd ROW ##########
        "opal_620_fluorophore": {"position": "B1", "volume": 250, "time": {"mins": 10, "sec": 0}},
        "empty": {"position": "B2", "volume": 0, "time": {"mins": 0, "sec": 0}},
        "empty": {"position": "B3", "volume": 0, "time": {"mins": 0, "sec": 0}},
        "empty": {"position": "A4", "volume": 0, "time": {"mins": 0, "sec": 0}},
        "empty": {"position": "B5", "volume": 0, "time": {"mins": 0, "sec": 0}},
        # 3rd ROW ##########
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

############ CLASS START ####################################################
class Opentron_Chacha:
    tip_count = 0
    location = {}

    def __init__(self, protocol, pipette, group, location, antibody_solution):
        self.protocol = protocol
        self.pipette = pipette
        self.group = group
        self.location = self.active_slide_chacha(location)
        self.antibody_solution = antibody_solution

    # remove all unactive slides
    def active_slide_chacha(self, location):
        for i in range(len(location)):
            if not location[i+1]["slides"][1]["active"]: del location[i+1]["slides"][1]
            if not location[i+1]["slides"][2]["active"]: del location[i+1]["slides"][2]
            if not location[i+1]["slides"][3]["active"]: del location[i+1]["slides"][3]
            if not location[i+1]["slides"][4]["active"]: del location[i+1]["slides"][4]
        return location
    
    # get chacha position
    def get_chacha(self, chacha):
        return self.group[chacha]

    # WASH OFF LIQUIDS
    def washing(self, row=1, wash_n_time=1):
        for i in range(wash_n_time):
            chacha_labware = self.get_chacha(1)
            if row != 1: chacha_labware = self.get_chacha(4)
            self.pipette.move_to(chacha_labware['A6'].top(20))
            self.pipette.move_to(chacha_labware['A6'].top(-10), speed=150)
            self.pipette.move_to(chacha_labware['A6'].top(-5))
            self.pipette.move_to(chacha_labware['A6'].top(-10), speed=150)
            self.protocol.delay(seconds=5)
            self.pipette.move_to(chacha_labware['L6'].top(20))
            self.pipette.move_to(chacha_labware['L6'].top(5), speed=150)
            self.pipette.move_to(chacha_labware['O6'].top(5), speed=150)
            self.pipette.move_to(chacha_labware['O6'].top(-1), speed=100)

    def get_position(self, antibody_type):
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

    def mix_up_n_down(self, volume, location, n_time):
        self.comment('MIX THE SOLUTION')
        for n in range(n_time):
            self.pipette.aspirate(volume, location)
            self.pipette.dispense(volume, location)
            self.pipette.blow_out(location)

    def get_max_volume_need(self, antibody_type):
        volume_need = self.get_volume(antibody_type)
        number_slide = self.slides_num
        max_volume = volume_need * number_slide
        return max_volume

    # blocking method
    def blocking_1000(self, antibody_type):
        self.tip_count += 1

        position = self.get_position(antibody_type)
        volume = self.get_volume(antibody_type)
        time = self.get_time(antibody_type)

        sol_labware = self.get_labware(antibody_type)

        max_vol_4_slides = self.get_max_volume_need(antibody_type)
        max_vol_pipette = self.pipette.max_volume

        volume_to_do = 0

        while(max_vol_4_slides > 0):

            if max_vol_4_slides <= max_vol_pipette:
                volume_to_do = max_vol_4_slides
            else:
                volume_to_do = max_vol_pipette

            self.mix_up_n_down(max_vol_pipette, sol_labware[position], 3)
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

        delay_min = time[0]
        delay_sec = time[1]

        self.comment(f'DELAY {delay_min} min, {delay_sec} sec')
        self.pipette.home()
        self.protocol.delay(minutes=delay_min, seconds=delay_sec)

    # NEW RINSING
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

############ CLASS END ####################################################


# Protocol Information
metadata = {
    'protocolName': "Opal 7 markers - 24 slides MAX",
    'author': "thuanvo",
    'description': "MASTER CHACHA",
    'apiLevel': "2.10"
}

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

    chacha_group = {1,2,3,4,5,6}

    if 1 in chacha_location and chacha_location[1]["active"] and isinstance(chacha_location[1]["position"], int): chacha_group[1] = protocol.load_labware(custom_chacha_code, chacha_location[1]["position"])
    else: del chacha_location[1]
    if 2 in chacha_location and chacha_location[2]["active"] and isinstance(chacha_location[2]["position"], int): chacha_group[2] = protocol.load_labware(custom_chacha_code, chacha_location[2]["position"])
    else: del chacha_location[2]
    if 3 in chacha_location and chacha_location[3]["active"] and isinstance(chacha_location[3]["position"], int): chacha_group[3] = protocol.load_labware(custom_chacha_code, chacha_location[3]["position"])
    else: del chacha_location[3]
    if 4 in chacha_location and chacha_location[4]["active"] and isinstance(chacha_location[4]["position"], int): chacha_group[4] = protocol.load_labware(custom_chacha_code, chacha_location[4]["position"])
    else: del chacha_location[4]
    if 5 in chacha_location and chacha_location[5]["active"] and isinstance(chacha_location[5]["position"], int): chacha_group[5] = protocol.load_labware(custom_chacha_code, chacha_location[5]["position"])
    else: del chacha_location[5]
    if 6 in chacha_location and chacha_location[6]["active"] and isinstance(chacha_location[6]["position"], int): chacha_group[6] = protocol.load_labware(custom_chacha_code, chacha_location[6]["position"])
    else: del chacha_location[6]

    tuberack_15 = protocol.load_labware(tuberack_15_code, tuberack_15_location)
    tbst_well = protocol.load_labware(custom_tbst_well_code, tbst_well_location)

    # Gather all solution information
    antibody_solution = antibody_def(tuberack_15, tbst_well)

#######################################################################
########## COMMANDS START #############################################
#######################################################################

    tasks = Opentron_Chacha(protocol, pipette, chacha_group,
                            chacha_location, antibody_solution)

    # Check Anti_body
    tasks.check_antibodies()

    tasks.comment('TASKS START AFTER 5 SECONDS')
    protocol.delay(minutes=0, seconds=5)

    ###################################################################
    ######## BLOCKING using Opal Antibody Dilluent ####################
    ###################################################################

    pipette.pick_up_tip()
    tasks.blocking_1000('opal_antibody_dilluent')
    tasks.washing(3)
    pipette.drop_tip()

    ###################################################################
    ######## PRIMARY ANTIBODY INCUBATION ##############################
    ###################################################################

    pipette.pick_up_tip()
    tasks.blocking_1000('cd8')
    tasks.washing(wash_n_time=3)
    pipette.drop_tip()

    ######## TBST #####################################################
    tasks.rinsing_with(antibody_type='tbst', n_time=6, n_each=1,
                       delay_min_in_btw=0, delay_sec_in_btw=30)

    ###################################################################
    ######## SECONDARY HRP ############################################
    ###################################################################

    pipette.pick_up_tip()
    tasks.blocking_1000('opal_polymer_HRP')
    tasks.washing(wash_n_time=3)
    pipette.drop_tip()

    ######## TBST #####################################################
    tasks.rinsing_with(antibody_type='tbst', n_time=6, n_each=1,
                       delay_min_in_btw=0, delay_sec_in_btw=30)

    ###################################################################
    ######## OPAL 690 FLUOROPHORE #####################################
    ###################################################################

    pipette.pick_up_tip()
    tasks.blocking_1000('opal_690_fluorophore')
    tasks.washing(wash_n_time=3)
    pipette.drop_tip()

    ######## TBST #####################################################
    tasks.rinsing_with(antibody_type='tbst', n_time=6, n_each=1,
                       delay_min_in_btw=0, delay_sec_in_btw=30)

    ###################################################################
    ######## PAUSE AND REFILL #########################################
    ###################################################################
    protocol.pause()
    tasks.comment(
        f"PLEASE REFILL [OPAL ANTIBODY DILLUENT] INTO {antibody_solution['opal_antibody_dilluent']['labware']} - {antibody_solution['opal_antibody_dilluent']['position']}\n")
    tasks.comment(
        f"PLEASE REFILL [OPAL POLYMER HRP]       INTO {antibody_solution['opal_polymer_HRP']['labware']} - {antibody_solution['opal_polymer_HRP']['position']}\n")
    tasks.comment(
        f"PLEASE PUT    [FoxP3]                  INTO {antibody_solution['foxp3']['labware']} - {antibody_solution['foxp3']['position']}\n")
    tasks.comment(
        f"PLEASE PUT       [Opal 620]               INTO {antibody_solution['opal_620_fluorophore']['labware']} - {antibody_solution['opal_620_fluorophore']['position']}\n")

    ###################################################################
    ######## BLOCKING using Opal Antibody Dilluent ####################
    ###################################################################

    pipette.pick_up_tip()
    tasks.blocking_1000('opal_antibody_dilluent')
    tasks.washing(3)
    pipette.drop_tip()

    pipette.pick_up_tip()
    tasks.blocking_1000('foxp3')
    tasks.washing(wash_n_time=3)
    pipette.drop_tip()

    ######## TBST #####################################################
    tasks.rinsing_with(antibody_type='tbst', n_time=6, n_each=1,
                       delay_min_in_btw=0, delay_sec_in_btw=30)

    ###################################################################
    ######## Secondary opal_polymer_HRP ####################
    ###################################################################

    pipette.pick_up_tip()
    tasks.blocking_1000('opal_polymer_HRP')
    tasks.washing(wash_n_time=3)
    pipette.drop_tip()

    ######## TBST #####################################################
    tasks.rinsing_with(antibody_type='tbst', n_time=6, n_each=1,
                       delay_min_in_btw=0, delay_sec_in_btw=30)

    pipette.pick_up_tip()
    tasks.blocking_1000('opal_620_fluorophore')
    tasks.washing(wash_n_time=3)
    pipette.drop_tip()

    ######## TBST #####################################################
    tasks.rinsing_with(antibody_type='tbst', n_time=6, n_each=1,
                       delay_min_in_btw=0, delay_sec_in_btw=30)


#######################################################################
########## COMMANDS END ###############################################
#######################################################################

    ######## REPORT VOLUME ############################################
    tasks.material_report()
