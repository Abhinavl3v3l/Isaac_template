#pragma once

#include "engine/alice/alice_codelet.hpp"
#include "messages/my_proto.hpp"

namespace isaac {
    class Receiver : public alice::Codelet {
        public:
            void start() override;
            void tick() override;

            ISAAC_PROTO_RX(MyCustomProto, number);
    };
}

ISAAC_ALICE_REGISTER_CODELET(isaac::Receiver);
