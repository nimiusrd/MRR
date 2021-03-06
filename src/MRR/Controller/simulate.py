from MRR.gragh import plot
from MRR.Evaluator import build_Evaluator
from MRR.Simulator import Ring, TransferFunction
from MRR.logger import Logger


def simulate(config_list, skip_plot, is_focus):
    logger = Logger()
    xs = []
    ys = []

    for config in config_list:
        number_of_rings = len(config['L'])
        config.setdefault('number_of_rings', number_of_rings)
        config.setdefault('FSR', 20e-9)
        config.setdefault('min_ring_length', 10e-9)
        config.setdefault('max_crosstalk', -30)
        config.setdefault('H_p', -20)
        config.setdefault('H_s', -60)
        config.setdefault('H_i', -10)
        config.setdefault('r_max', 5)
        config.setdefault('length_of_3db_band', 1e-9)
        Evaluator = build_Evaluator(config)

        mrr = TransferFunction(
            config['L'],
            config['K'],
            config
        )
        mrr.print_parameters()
        ring = Ring(config)
        N = ring.calculate_N(config['L'])
        FSR = ring.calculate_practical_FSR(N)
        print(FSR)

        if 'lambda' in config:
            x = config['lambda']
            y = mrr.simulate(x)
        else:
            x = ring.calculate_x(FSR)
            y = mrr.simulate(x)
            evaluator = Evaluator(
                x,
                y
            )
            result = evaluator.evaluate_band()
            print(result)

        logger.save_data_as_csv(x, y, config['name'])
        xs.append(x)
        ys.append(y)

    if not skip_plot:
        plot(xs, ys, config['L'].size, logger.generate_image_path(config['name']), is_focus)
