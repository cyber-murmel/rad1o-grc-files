#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Jul 26 13:43:39 2016
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr


class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.trans_width = trans_width = 20e3
        self.samp_rate = samp_rate = int(2e6)
        self.cutoff = cutoff = 16e3
        self.chan_3 = chan_3 = 466.235e6
        self.chan_2 = chan_2 = 466.080e6
        self.chan_1 = chan_1 = 465.975e6
        self.base_freq = base_freq = 465e6
        self.audio_rate = audio_rate = int(22.05e3)

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=audio_rate,
                decimation=samp_rate,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(base_freq, 0)
        self.osmosdr_source_0.set_freq_corr(13, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(0, 0)
        self.osmosdr_source_0.set_if_gain(24, 0)
        self.osmosdr_source_0.set_bb_gain(18, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0_0_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, cutoff, trans_width, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, cutoff, trans_width, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, cutoff, trans_width, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, cutoff, trans_width, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.audio_sink_0 = audio.sink(audio_rate, "", True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=samp_rate,
        	audio_decimation=1,
        )
        self.analog_sig_source_x_0_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, base_freq-chan_3, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, base_freq-chan_2, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, base_freq-chan_1, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 0))    
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 0))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.low_pass_filter_0_0_0_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.low_pass_filter_0_0_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.low_pass_filter_0_0_0, 0), (self.blocks_add_xx_0, 2))    
        self.connect((self.low_pass_filter_0_0_0_0, 0), (self.analog_wfm_rcv_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_0_0, 1))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.audio_sink_0, 0))    

    def get_trans_width(self):
        return self.trans_width

    def set_trans_width(self, trans_width):
        self.trans_width = trans_width
        self.low_pass_filter_0_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.trans_width, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.trans_width, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.trans_width, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.trans_width, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.trans_width, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.trans_width, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.trans_width, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.trans_width, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff
        self.low_pass_filter_0_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.trans_width, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.trans_width, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.trans_width, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.trans_width, firdes.WIN_HAMMING, 6.76))

    def get_chan_3(self):
        return self.chan_3

    def set_chan_3(self, chan_3):
        self.chan_3 = chan_3
        self.analog_sig_source_x_0_0_0.set_frequency(self.base_freq-self.chan_3)

    def get_chan_2(self):
        return self.chan_2

    def set_chan_2(self, chan_2):
        self.chan_2 = chan_2
        self.analog_sig_source_x_0_0.set_frequency(self.base_freq-self.chan_2)

    def get_chan_1(self):
        return self.chan_1

    def set_chan_1(self, chan_1):
        self.chan_1 = chan_1
        self.analog_sig_source_x_0.set_frequency(self.base_freq-self.chan_1)

    def get_base_freq(self):
        return self.base_freq

    def set_base_freq(self, base_freq):
        self.base_freq = base_freq
        self.osmosdr_source_0.set_center_freq(self.base_freq, 0)
        self.analog_sig_source_x_0_0_0.set_frequency(self.base_freq-self.chan_3)
        self.analog_sig_source_x_0_0.set_frequency(self.base_freq-self.chan_2)
        self.analog_sig_source_x_0.set_frequency(self.base_freq-self.chan_1)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
