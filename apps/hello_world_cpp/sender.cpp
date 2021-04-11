#include "sender.hpp"

namespace isaac {
    void Sender::start() {
        tickPeriodically();
    }

    void Sender::tick() {
        auto proto = tx_number().initProto();
        proto.setMyValue(get_number());
        tx_number().publish();
    }
}