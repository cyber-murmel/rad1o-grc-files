#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Sep  6 21:34:13 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.pmr_channel = pmr_channel = 1
        self.base_freq = base_freq = 446.0e6+12.5e3
        self.trans_width = trans_width = 8e3
        self.samp_rate = samp_rate = 0.25e6
        self.freq = freq = base_freq+12.5e3*(pmr_channel-1)
        self.cutoff_freq = cutoff_freq = 10e3
        self.audio_samp_rate = audio_samp_rate = 48e3

        ##################################################
        # Blocks
        ##################################################
        _trans_width_sizer = wx.BoxSizer(wx.VERTICAL)
        self._trans_width_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_trans_width_sizer,
        	value=self.trans_width,
        	callback=self.set_trans_width,
        	label="Transition Width",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._trans_width_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_trans_width_sizer,
        	value=self.trans_width,
        	callback=self.set_trans_width,
        	minimum=1e3,
        	maximum=50e3,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_trans_width_sizer, 0, 2, 1, 1)
        _cutoff_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._cutoff_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_cutoff_freq_sizer,
        	value=self.cutoff_freq,
        	callback=self.set_cutoff_freq,
        	label='cutoff_freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._cutoff_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_cutoff_freq_sizer,
        	value=self.cutoff_freq,
        	callback=self.set_cutoff_freq,
        	minimum=1e3,
        	maximum=50e3,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_cutoff_freq_sizer, 0, 1, 1, 1)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=int(samp_rate)/5,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=int(audio_samp_rate),
                decimation=int(samp_rate)/5,
                taps=None,
                fractional_bw=None,
        )
        self._pmr_channel_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.pmr_channel,
        	callback=self.set_pmr_channel,
        	label="Channel",
        	choices=[1,2,3,4,5,6,7,8],
        	labels=[],
        	style=wx.RA_HORIZONTAL,
        )
        self.GridAdd(self._pmr_channel_chooser, 0, 0, 1, 1)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(863.123, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(2, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(0, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	2, samp_rate, cutoff_freq, trans_width, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((1, ))
        self.audio_sink_0 = audio.sink(int(audio_samp_rate), "", True)
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=int(samp_rate)/5,
        	quad_rate=int(samp_rate),
        	tau=75e-6,
        	max_dev=5e3,
          )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_rx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.analog_nbfm_rx_0, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_nbfm_rx_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    

    def get_pmr_channel(self):
        return self.pmr_channel

    def set_pmr_channel(self, pmr_channel):
        self.pmr_channel = pmr_channel
        self._pmr_channel_chooser.set_value(self.pmr_channel)
        self.set_freq(self.base_freq+12.5e3*(self.pmr_channel-1))

    def get_base_freq(self):
        return self.base_freq

    def set_base_freq(self, base_freq):
        self.base_freq = base_freq
        self.set_freq(self.base_freq+12.5e3*(self.pmr_channel-1))

    def get_trans_width(self):
        return self.trans_width

    def set_trans_width(self, trans_width):
        self.trans_width = trans_width
        self._trans_width_slider.set_value(self.trans_width)
        self._trans_width_text_box.set_value(self.trans_width)
        self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, self.cutoff_freq, self.trans_width, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(int(self.samp_rate)/5)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, self.cutoff_freq, self.trans_width, firdes.WIN_HAMMING, 6.76))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_cutoff_freq(self):
        return self.cutoff_freq

    def set_cutoff_freq(self, cutoff_freq):
        self.cutoff_freq = cutoff_freq
        self._cutoff_freq_slider.set_value(self.cutoff_freq)
        self._cutoff_freq_text_box.set_value(self.cutoff_freq)
        self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, self.cutoff_freq, self.trans_width, firdes.WIN_HAMMING, 6.76))

    def get_audio_samp_rate(self):
        return self.audio_samp_rate

    def set_audio_samp_rate(self, audio_samp_rate):
        self.audio_samp_rate = audio_samp_rate


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
