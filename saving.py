max_vol_aspirate = self.pipette.max_volume
        volume_to_do = 0
        

        while (volume > 0):

            if (volume > max_vol_aspirate):
                volume_to_do = max_vol_aspirate
            else:
                volume_to_do = volume
            
            self.comment(f'BLOCK WITH {volume_to_do} uL {antibody_type} FROM {sol_labware} - {position}')

            for i in range(self.slides_num):
                self.mix_up_n_down(max_vol_aspirate, sol_labware[position], 3)
                self.pipette.aspirate(volume_to_do, sol_labware[position])
                self.volume_used(antibody_type, volume_to_do)

                self.pipette.move_to(sol_labware[position].top(20), speed=50) # move slowly up

                for col in self.blocking_position[f'slide{i+1}']['cols']:
                    for row in self.blocking_position[f'slide{i+1}']['rows']:
                        self.pipette.dispense(volume_to_do/4, location=self.chacha_labware[row+col].top(5))

                #
                last_row_pos = self.blocking_position[f'slide{i+1}']['rows'][-1]
                last_col_pos = self.blocking_position[f'slide{i+1}']['cols'][-1]
                last_drop_position = self.chacha_labware[last_row_pos+last_col_pos]
                while (self.pipette.current_volume > 0):
                    self.pipette.dispense(self.pipette.current_volume, location=last_drop_position.top(5))
                self.pipette.blow_out(location=last_drop_position.top(5))
                #
            
            volume -= volume_to_do