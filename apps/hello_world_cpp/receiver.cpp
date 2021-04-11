#include "receiver.hpp"
#include <string>

namespace isaac {
    void Receiver::start() {
        tickOnMessage(rx_number());
    }

    void Receiver::tick() {
        auto proto = rx_number().getProto();

        const int number = proto.getMyValue();

        LOG_INFO(std::to_string(number).c_str());
    }
}
