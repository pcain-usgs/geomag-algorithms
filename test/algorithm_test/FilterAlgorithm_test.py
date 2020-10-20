from geomagio.algorithm import FilterAlgorithm
from obspy.core import read
import geomagio.iaga2002 as i2
from numpy.testing import assert_almost_equal


def test_second():
    """algorithm_test.FilterAlgorithm_test.test_second()
    Tests algorithm for 10Hz to second.
    """
    f = FilterAlgorithm(input_sample_period=0.1, output_sample_period=1)

    # generation of 10HZ_filter_sec.mseed
    # starttime = UTCDateTime('2020-01-06T00:00:00Z')
    # endtime = UTCDateTime('2020-01-06T04:00:00Z')
    # m = MiniSeedFactory(port=2061, host='...',
    #       convert_channels=['U', 'V', 'W'],
    #       bin_conv=500, volt_conv=100)
    # f = FilterAlgorithm(input_sample_period=0.1,
    #       output_sample_period=1.0)
    # starttime, endtime = f.get_input_interval(starttime,endtime)
    # LLO_raw = m.get_timeseries(observatory='LLO',
    #       starttime=starttime,endtime=endtime,
    #       channels=['U_Volt', 'U_Bin', 'V_Volt',
    #                 'V_Bin', 'W_Volt', 'W_Bin'],
    #       interval='tenhertz', type='variaton')
    # LLO_raw.write('10HZ_filter_sec.mseed')

    llo = read("etc/filter/10HZ_filter_sec.mseed")
    filtered = f.process(llo)

    with open("etc/filter/LLO20200106vsec.sec", "r") as f:
        iaga = i2.StreamIAGA2002Factory(stream=f)
        LLO = iaga.get_timeseries(starttime=None, endtime=None, observatory="LLO")

    u = LLO.select(channel="U")[0]
    v = LLO.select(channel="V")[0]
    w = LLO.select(channel="W")[0]

    u_filt = filtered.select(channel="U")[0]
    v_filt = filtered.select(channel="V")[0]
    w_filt = filtered.select(channel="W")[0]

    assert_almost_equal(u_filt.data, u.data, 2)
    assert_almost_equal(v_filt.data, v.data, 2)
    assert_almost_equal(w_filt.data, w.data, 2)


def test_minute():
    """algorithm_test.FilterAlgorithm_test.test_minute()
    Tests algorithm for 10Hz to minute.
    """
    f = FilterAlgorithm(input_sample_period=0.1, output_sample_period=60.0)

    # generation of 10HZ_filter_min.mseed
    # starttime = UTCDateTime('2020-01-06T00:00:00Z')
    # endtime = UTCDateTime('2020-01-06T04:00:00Z')
    # m = MiniSeedFactory(port=2061, host='...',
    #       convert_channels=['U', 'V', 'W'])
    # f = FilterAlgorithm(input_sample_period=0.1,
    #       output_sample_period=60.0)
    # starttime, endtime = f.get_input_interval(starttime,endtime)
    # LLO = m.get_timeseries(observatory='LLO',
    #       starttime=starttime,endtime=endtime,
    #       channels=['U_Volt', 'U_Bin', 'V_Volt',
    #                 'V_Bin', 'W_Volt', 'W_Bin'],
    #       interval='tenhertz', type='variaton')
    # LLO.write('10HZ_filter_min.mseed')

    llo = read("etc/filter/10HZ_filter_min.mseed")
    filtered = f.process(llo)

    with open("etc/filter/LLO20200106vmin.min", "r") as f:
        iaga = i2.StreamIAGA2002Factory(stream=f)
        LLO = iaga.get_timeseries(starttime=None, endtime=None, observatory="LLO")

    u = LLO.select(channel="U")[0]
    v = LLO.select(channel="V")[0]
    w = LLO.select(channel="W")[0]

    u_filt = filtered.select(channel="U")[0]
    v_filt = filtered.select(channel="V")[0]
    w_filt = filtered.select(channel="W")[0]

    assert_almost_equal(u_filt.data, u.data, 2)
    assert_almost_equal(v_filt.data, v.data, 2)
    assert_almost_equal(w_filt.data, w.data, 2)


def test_hour():
    """algorithm_test.FilterAlgorithm_test.test_hour()
    Tests algorithm for 10Hz to hour.
    """
    f = FilterAlgorithm(input_sample_period=0.1, output_sample_period=3600.0)

    # generation of 10HZ_filter_hor.mseed
    # starttime = UTCDateTime('2020-01-06T00:00:00Z')
    # endtime = UTCDateTime('2020-01-06T04:00:00Z')
    # m = MiniSeedFactory(port=2061, host='...',
    #       convert_channels=['U', 'V', 'W'])
    # f = FilterAlgorithm(input_sample_period=0.1,
    #       output_sample_period=3600.0)
    # starttime, endtime = f.get_input_interval(starttime,endtime)
    # LLO = m.get_timeseries(observatory='LLO',
    #       starttime=starttime,endtime=endtime,
    #       channels=['U_Volt', 'U_Bin', 'V_Volt',
    #                 'V_Bin', 'W_Volt', 'W_Bin'],
    #       interval='tenhertz', type='variaton')
    # LLO.write('10HZ_filter_hor.mseed')

    llo = read("etc/filter/10HZ_filter_hor.mseed")
    filtered = f.process(llo)

    with open("etc/filter/LLO20200106vhor.hor", "r") as f:
        iaga = i2.StreamIAGA2002Factory(stream=f)
        LLO = iaga.get_timeseries(starttime=None, endtime=None, observatory="LLO")

    u = LLO.select(channel="U")[0]
    v = LLO.select(channel="V")[0]
    w = LLO.select(channel="W")[0]

    u_filt = filtered.select(channel="U")[0]
    v_filt = filtered.select(channel="V")[0]
    w_filt = filtered.select(channel="W")[0]

    assert_almost_equal(u_filt.data, u.data, 2)
    assert_almost_equal(v_filt.data, v.data, 2)
    assert_almost_equal(w_filt.data, w.data, 2)


def test_custom():
    """algorithm_test.FilterAlgorithm_test.test_custom()
    Tests algorithm for 10Hz to second with custom filter coefficients.
    """
    f = FilterAlgorithm(
        input_sample_period=0.1,
        output_sample_period=1.0,
        coeff_filename="etc/filter/coeffs.json",
    )

    # generation of 10HZ_filter_sec.mseed
    # starttime = UTCDateTime('2020-01-06T00:00:00Z')
    # endtime = UTCDateTime('2020-01-06T04:00:00Z')
    # m = MiniSeedFactory(port=2061, host='...',
    #       convert_channels=['U', 'V', 'W'])
    # f = FilterAlgorithm(input_sample_period=0.1,
    #       output_sample_period=1.0)
    # starttime, endtime = f.get_input_interval(starttime,endtime)
    # LLO = m.get_timeseries(observatory='LLO',
    #       starttime=starttime,endtime=endtime,
    #       channels=['U_Volt', 'U_Bin', 'V_Volt',
    #                 'V_Bin', 'W_Volt', 'W_Bin'],
    #       interval='tenhertz', type='variaton')
    # LLO.write('10HZ_filter_sec.mseed')

    llo = read("etc/filter/10HZ_filter_sec.mseed")
    filtered = f.process(llo)

    with open("etc/filter/LLO20200106_custom_vsec.sec", "r") as f:
        iaga = i2.StreamIAGA2002Factory(stream=f)
        LLO = iaga.get_timeseries(starttime=None, endtime=None, observatory="LLO")

    u = LLO.select(channel="U")[0]
    v = LLO.select(channel="V")[0]
    w = LLO.select(channel="W")[0]

    u_filt = filtered.select(channel="U")[0]
    v_filt = filtered.select(channel="V")[0]
    w_filt = filtered.select(channel="W")[0]

    assert_almost_equal(u_filt.data, u.data, 2)
    assert_almost_equal(v_filt.data, v.data, 2)
    assert_almost_equal(w_filt.data, w.data, 2)


def test_starttime_shift():
    """algorithm_test.FilterAlgorithm_test.test_starttime_shift()
    Tests algorithm for second to minute with misalligned starttime(16 seconds).
    """
    f = FilterAlgorithm(input_sample_period=1.0, output_sample_period=60.0,)
    # generation of BOU20200101vsec.sec
    # starttime = UTCDateTime('2020-01-01T00:00:00Z')
    # endtime = UTCDateTime('2020-01-01T00:15:00Z')
    # starttime,endtime = f.get_input_interval(starttime,endtime)
    # bou = e.get_timeseries(observatory='BOU',interval='second',type='variation',starttime=starttime,endtime=endtime,channels=["H","E","Z","F"])
    # with open('BOU20200101vsec.sec','wb') as file:
    #     i2w.write(out=file,timeseries=bou,channels=["H","E","Z","F"])
    with open("etc/filter/BOU20200101vsec.sec", "r") as file:
        iaga = i2.StreamIAGA2002Factory(stream=file)
        bou = iaga.get_timeseries(starttime=None, endtime=None, observatory="BOU")
    # gather starttime and endtime from stream
    starttime = bou[0].stats.starttime
    endtime = bou[0].stats.endtime
    # apply offset of 16 seconds to starttime to generate misaligned stream
    bou_misaligned = bou.trim(starttime=starttime + 16, endtime=endtime)
    # process both streams with FilterAlgorithm
    bou_filtered = f.process(bou)
    bou_misaligned_filtered = f.process(bou_misaligned)
    # compare starttimes and dimensions of data to detect correct offset in output
    len(bou_filtered[0].data) - len(bou_misaligned_filtered[0].data) == (
        bou_misaligned_filtered[0].stats.starttime - bou_filtered[0].stats.starttime
    ) / f.output_sample_period
